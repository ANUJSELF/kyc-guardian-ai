import React from 'react'
import { Stack, Text } from '@fluentui/react'

const AuditTrail: React.FC = () => {
  return (
    <Stack tokens={{ childrenGap: 16 }}>
      <Text size={500} weight="bold">
        Audit Trail & Evidence
      </Text>
      <Text size={200}>Complete case processing history and evidence</Text>
    </Stack>
  )
}

export default AuditTrail
