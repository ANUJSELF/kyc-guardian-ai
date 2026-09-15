import React, { useState } from 'react'
import { Stack, TextField, Dropdown, PrimaryButton, DefaultButton, MessageBar, MessageBarType } from '@fluentui/react'
import { useNavigate } from 'react-router-dom'
import { caseService } from '../services/caseService'
import { MARKETS, DEMO_DISCLAIMER } from '../constants'

const CreateCase: React.FC = () => {
  const navigate = useNavigate()
  const [applicantType, setApplicantType] = useState('individual')
  const [market, setMarket] = useState('')
  const [description, setDescription] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleCreate = async () => {
    if (!market) {
      setError('Please select a market')
      return
    }

    setLoading(true)
    try {
      const newCase = await caseService.create({
        applicant_type: applicantType,
        market,
        onboarding_journey: 'Standard',
        description,
        reviewer: 'Reviewer Demo',
      })
      navigate(`/cases/${newCase.id}/workspace`)
    } catch (err) {
      setError('Failed to create case')
    } finally {
      setLoading(false)
    }
  }

  return (
    <Stack tokens={{ childrenGap: 16 }} style={{ maxWidth: 600 }}>
      <MessageBar messageBarType={MessageBarType.warning}>
        ⚠️ {DEMO_DISCLAIMER}
      </MessageBar>

      {error && (
        <MessageBar messageBarType={MessageBarType.error}>
          {error}
        </MessageBar>
      )}

      <Dropdown
        label="Applicant Type"
        options={[
          { key: 'individual', text: 'Individual' },
          { key: 'business', text: 'Business' },
        ]}
        selectedKey={applicantType}
        onChange={(e, option) => setApplicantType(option?.key as string)}
      />

      <Dropdown
        label="Market *"
        options={MARKETS}
        selectedKey={market}
        onChange={(e, option) => setMarket(option?.key as string)}
      />

      <TextField
        label="Description"
        multiline
        rows={4}
        value={description}
        onChange={(e, value) => setDescription(value || '')}
      />

      <Stack horizontal tokens={{ childrenGap: 8 }}>
        <PrimaryButton onClick={handleCreate} disabled={loading} text="Create Case" />
        <DefaultButton onClick={() => navigate('/cases')} text="Cancel" />
      </Stack>
    </Stack>
  )
}

export default CreateCase
