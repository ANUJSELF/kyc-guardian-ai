import React from 'react'
import { Stack, Text, MessageBar, MessageBarType } from '@fluentui/react'

const SystemInfo: React.FC = () => {
  return (
    <Stack tokens={{ childrenGap: 16 }}>
      <Text size={500} weight="bold">
        System Information
      </Text>

      <MessageBar messageBarType={MessageBarType.info}>
        System Configuration & Status
      </MessageBar>

      <div className="info-card">
        <Text size={300} weight="bold">
          AI Service Configuration
        </Text>
        <Text size={200}>AI Service: Mock (Default - No Internet Required)</Text>
        <Text size={200}>Optional: Ollama Local Integration Available</Text>
      </div>

      <div className="info-card">
        <Text size={300} weight="bold">
          Data Security
        </Text>
        <Text size={200}>✅ Local Processing Only</Text>
        <Text size={200}>✅ No External API Calls</Text>
        <Text size={200}>✅ Automatic PII Masking</Text>
        <Text size={200}>✅ Append-Only Audit Trail</Text>
      </div>

      <div className="info-card">
        <Text size={300} weight="bold">
          Feature Status
        </Text>
        <Text size={200}>✅ Document Upload & Processing</Text>
        <Text size={200}>✅ OCR & Classification</Text>
        <Text size={200}>✅ Field Extraction</Text>
        <Text size={200}>✅ Cross-Document Comparison</Text>
        <Text size={200}>✅ Exception Management</Text>
        <Text size={200}>✅ Audit Trail & Evidence Export</Text>
      </div>
    </Stack>
  )
}

export default SystemInfo
