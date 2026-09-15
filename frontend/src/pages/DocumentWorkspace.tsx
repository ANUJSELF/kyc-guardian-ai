import React from 'react'
import { Stack, Text } from '@fluentui/react'

const DocumentWorkspace: React.FC = () => {
  return (
    <Stack tokens={{ childrenGap: 16 }}>
      <Text size={500} weight="bold">
        Document Workspace
      </Text>
      <Text size={200}>Upload and review documents for your case</Text>
    </Stack>
  )
}

export default DocumentWorkspace
