import React from 'react'
import { Stack, Text } from '@fluentui/react'

const ReviewQueue: React.FC = () => {
  return (
    <Stack tokens={{ childrenGap: 16 }}>
      <Text size={500} weight="bold">
        Review Queue
      </Text>
      <Text size={200}>Cases awaiting human review</Text>
    </Stack>
  )
}

export default ReviewQueue
