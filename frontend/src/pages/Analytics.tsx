import React from 'react'
import { Stack, Text } from '@fluentui/react'

const Analytics: React.FC = () => {
  return (
    <Stack tokens={{ childrenGap: 16 }}>
      <Text size={500} weight="bold">
        Analytics
      </Text>
      <Text size={200}>Processing and performance metrics</Text>
    </Stack>
  )
}

export default Analytics
