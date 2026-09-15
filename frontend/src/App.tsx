import { Routes, Route } from 'react-router-dom'
import { FluentProvider, teamsLightTheme } from '@fluentui/react-components'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import Cases from './pages/Cases'
import CreateCase from './pages/CreateCase'
import DocumentWorkspace from './pages/DocumentWorkspace'
import ReviewQueue from './pages/ReviewQueue'
import Analytics from './pages/Analytics'
import AuditTrail from './pages/AuditTrail'
import SystemInfo from './pages/SystemInfo'
import './App.css'

function App() {
  return (
    <FluentProvider theme={teamsLightTheme}>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/cases" element={<Cases />} />
          <Route path="/cases/create" element={<CreateCase />} />
          <Route path="/cases/:caseId/workspace" element={<DocumentWorkspace />} />
          <Route path="/review-queue" element={<ReviewQueue />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route path="/audit-trail/:caseId" element={<AuditTrail />} />
          <Route path="/system-info" element={<SystemInfo />} />
        </Routes>
      </Layout>
    </FluentProvider>
  )
}

export default App
