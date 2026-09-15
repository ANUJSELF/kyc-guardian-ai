import React, { useEffect, useState } from 'react'
import { Stack, Text, Spinner, MessageBar, MessageBarType } from '@fluentui/react'
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'
import { analyticsService } from '../services/analyticsService'

interface Metrics {
  total_cases: number
  cases_requiring_review: number
  documents_processed: number
  low_confidence_fields: number
  reviewer_corrections: number
  average_processing_time_minutes: number
  exceptions_by_type: Record<string, number>
}

const Dashboard: React.FC = () => {
  const [metrics, setMetrics] = useState<Metrics | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchMetrics = async () => {
      try {
        const data = await analyticsService.getDashboard()
        setMetrics(data)
      } catch (err) {
        setError('Failed to load dashboard metrics')
      } finally {
        setLoading(false)
      }
    }

    fetchMetrics()
  }, [])

  if (loading) return <Spinner label="Loading dashboard..." />

  return (
    <Stack tokens={{ childrenGap: 16 }}>
      <MessageBar messageBarType={MessageBarType.info}>
        ℹ️ All figures are generated from synthetic prototype data and do not represent production results or realised business benefits.
      </MessageBar>

      {error && (
        <MessageBar messageBarType={MessageBarType.error}>
          {error}
        </MessageBar>
      )}

      {metrics && (
        <>
          <Stack horizontal tokens={{ childrenGap: 16 }}>
            <div className="metric-card">
              <Text size={500} weight="bold">
                {metrics.total_cases}
              </Text>
              <Text size={200}>Total Cases</Text>
            </div>
            <div className="metric-card">
              <Text size={500} weight="bold">
                {metrics.cases_requiring_review}
              </Text>
              <Text size={200}>Requiring Review</Text>
            </div>
            <div className="metric-card">
              <Text size={500} weight="bold">
                {metrics.documents_processed}
              </Text>
              <Text size={200}>Documents Processed</Text>
            </div>
            <div className="metric-card">
              <Text size={500} weight="bold">
                {metrics.reviewer_corrections}
              </Text>
              <Text size={200}>Reviewer Corrections</Text>
            </div>
          </Stack>

          <div className="chart-container">
            <Text size={400} weight="bold">
              Exceptions by Category
            </Text>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={Object.entries(metrics.exceptions_by_type).map(([key, value]) => ({ name: key, count: value }))}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="count" fill="#ff9500" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </>
      )}
    </Stack>
  )
}

export default Dashboard
