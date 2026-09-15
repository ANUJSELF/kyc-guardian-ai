import React from 'react'
import { Stack, Text, PrimaryButton } from '@fluentui/react'

const Cases: React.FC = () => {
  return (
    <Stack tokens={{ childrenGap: 16 }}>
      <div>
        <Text size={500} weight="bold">
          Cases
        </Text>
        <Text size={200}>Manage and review KYC/KYB cases</Text>
      </div>
      <PrimaryButton href="/cases/create">Create New Case</PrimaryButton>
    </Stack>
  )
}

export default Cases
