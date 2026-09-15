import React from 'react'
import { Stack, Text } from '@fluentui/react'
import './Header.css'

const Header: React.FC = () => {
  return (
    <header className="header">
      <Stack horizontal verticalAlign="center" tokens={{ childrenGap: 8 }}>
        <div className="header-content">
          <Text size={600} weight="bold">
            KYC Guardian AI - Document Intelligence Platform
          </Text>
          <Text size={200} color="gray">
            AI-Powered KYC/KYB Document Processing with Evidence Management
          </Text>
        </div>
      </Stack>
    </header>
  )
}

export default Header
