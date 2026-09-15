import React from 'react'
import { useNavigate, useLocation } from 'react-router-dom'
import { Nav, INavLink, Stack, Text } from '@fluentui/react'
import './Navigation.css'

const Navigation: React.FC = () => {
  const navigate = useNavigate()
  const location = useLocation()

  const navLinks: INavLink[] = [
    {
      name: '📊 Dashboard',
      url: '/',
      onClick: () => navigate('/'),
    },
    {
      name: '📁 Cases',
      url: '/cases',
      onClick: () => navigate('/cases'),
    },
    {
      name: '➕ Create Case',
      url: '/cases/create',
      onClick: () => navigate('/cases/create'),
    },
    {
      name: '📋 Review Queue',
      url: '/review-queue',
      onClick: () => navigate('/review-queue'),
    },
    {
      name: '📈 Analytics',
      url: '/analytics',
      onClick: () => navigate('/analytics'),
    },
    {
      name: '🔍 Audit & Evidence',
      url: '/audit-trail',
      onClick: () => navigate('/audit-trail/'),
    },
    {
      name: '⚙️ System Info',
      url: '/system-info',
      onClick: () => navigate('/system-info'),
    },
  ]

  return (
    <nav className="navigation">
      <Stack tokens={{ childrenGap: 8 }}>
        <div className="nav-header">
          <Text size={500} weight="bold">
            🛡️ KYC Guardian AI
          </Text>
        </div>
        <Nav
          selectedKey={location.pathname}
          links={navLinks}
          styles={{
            link: {
              fontSize: 14,
              paddingLeft: 12,
            },
          }}
        />
      </Stack>
    </nav>
  )
}

export default Navigation
