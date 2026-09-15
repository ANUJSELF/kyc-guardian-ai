import React from 'react'
import { Outlet } from 'react-router-dom'
import Navigation from './Navigation'
import Header from './Header'
import { DEMO_DISCLAIMER } from '../constants'
import './Layout.css'

interface LayoutProps {
  children: React.ReactNode
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  return (
    <div className="layout-container">
      <div className="disclaimer-banner">
        <span>⚠️ {DEMO_DISCLAIMER}</span>
      </div>
      <div className="layout-body">
        <Navigation />
        <div className="layout-main">
          <Header />
          <div className="layout-content">
            {children}
            <Outlet />
          </div>
        </div>
      </div>
    </div>
  )
}

export default Layout
