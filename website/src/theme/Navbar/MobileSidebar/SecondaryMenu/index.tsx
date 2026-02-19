/**
 * Swizzled NavbarMobileSidebarSecondaryMenu component
 * Ensures the docs sidebar items are properly rendered in mobile hamburger menu
 */
import React from 'react';
import {useNavbarSecondaryMenu} from '@docusaurus/theme-common/internal';
import type {Props} from '@theme/Navbar/MobileSidebar/SecondaryMenu';

// This renders the secondary menu content (docs sidebar when on a docs page)
function SecondaryMenuContent(): JSX.Element | null {
  const secondaryMenu = useNavbarSecondaryMenu();
  return secondaryMenu.content;
}

export default function NavbarMobileSidebarSecondaryMenu({
  toggleSidebar,
}: Props): JSX.Element | null {
  const secondaryMenu = useNavbarSecondaryMenu();

  if (!secondaryMenu.shown) {
    return null;
  }

  return (
    <div 
      className="navbar-sidebar__item navbar-sidebar__items--show-secondary"
      style={{
        display: 'block',
        visibility: 'visible',
        opacity: 1,
      }}
    >
      <button 
        type="button" 
        className="clean-btn navbar-sidebar__back"
        onClick={() => secondaryMenu.hide()}
      >
        ← Back to main menu
      </button>
      <div className="menu" style={{display: 'block'}}>
        <SecondaryMenuContent />
      </div>
    </div>
  );
}
