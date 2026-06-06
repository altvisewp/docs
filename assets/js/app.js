/* AltviseWP Docs — app.js */
( function () {
  'use strict';

  // ── Search index ────────────────────────────────────────
  // Generated from all doc pages — titles, sections, and excerpts
  const SEARCH_INDEX = [
    // Footnotes Made Easy (free)
    { title: 'Overview', section: 'Footnotes Made Easy', url: '/footnotes-made-easy/index', excerpt: 'Free WordPress plugin for adding professional footnotes to posts and pages using simple inline syntax.' },
    { title: 'Installation', section: 'Footnotes Made Easy', url: '/footnotes-made-easy/installation', excerpt: 'Install from WordPress dashboard, upload ZIP, or manual FTP. Requirements: WordPress 6.0, PHP 7.4.' },
    { title: 'Getting Started', section: 'Footnotes Made Easy', url: '/footnotes-made-easy/getting-started', excerpt: 'Wrap footnote text in double parentheses (( )) anywhere in your content. Automatic numbering and linking.' },
    { title: 'Settings — Display', section: 'Footnotes Made Easy › Settings', url: '/footnotes-made-easy/settings/display', excerpt: 'Configure footnote identifiers, back links, header and footer text, and tooltip behaviour.' },
    { title: 'Settings — Behaviour', section: 'Footnotes Made Easy › Settings', url: '/footnotes-made-easy/settings/behaviour', excerpt: 'Back link position, combining identical footnotes, processing priority.' },
    { title: 'Settings — Suppress', section: 'Footnotes Made Easy › Settings', url: '/footnotes-made-easy/settings/suppress', excerpt: 'Hide footnotes on homepage, archives, feeds, specific post types, or custom URLs.' },
    { title: 'Settings — Advanced', section: 'Footnotes Made Easy › Settings', url: '/footnotes-made-easy/settings/advanced', excerpt: 'Change delimiters from (( )) to custom opening and closing tags. Shortcode support.' },
    { title: 'Tools', section: 'Footnotes Made Easy', url: '/footnotes-made-easy/tools', excerpt: 'Export and import settings as JSON. Factory reset. Preserve settings on uninstall.' },
    { title: 'Multisite', section: 'Footnotes Made Easy', url: '/footnotes-made-easy/multisite', excerpt: 'Network managed mode or per-subsite override. Configure from network admin.' },
    { title: 'FAQ', section: 'Footnotes Made Easy', url: '/footnotes-made-easy/faq', excerpt: 'Frequently asked questions about installation, settings, compatibility, and the Pro version.' },
    { title: 'Changelog', section: 'Footnotes Made Easy', url: '/footnotes-made-easy/changelog', excerpt: 'Release history. Version 3.2.0 includes new admin UI, export/import, multisite, and Pro coming soon page.' },
    // Pro
    { title: 'Pro — Installation', section: 'Footnotes Made Easy Pro', url: '/footnotes-made-easy/pro-installation', excerpt: 'Download from your account, install via WordPress dashboard. Requires free plugin to be active.' },
    { title: 'License Activation', section: 'Footnotes Made Easy Pro', url: '/footnotes-made-easy/pro-license-activation', excerpt: 'Enter license key at Footnotes → License. Activation limits, deactivation, transfer, multisite.' },
    { title: 'Citations — Overview', section: 'Footnotes Made Easy Pro › Citations', url: '/footnotes-made-easy/pro-citations-overview', excerpt: 'APA, MLA, and Chicago citation formatting. DOI and ISBN auto-fetch. Set default citation style.' },
    { title: 'Citations — Source Types', section: 'Footnotes Made Easy Pro › Citations', url: '/footnotes-made-easy/pro-citations-source-types', excerpt: '10 source types: book, journal article, website, newspaper, magazine, film, thesis, book chapter, conference paper, other.' },
    { title: 'Citations — Styles', section: 'Footnotes Made Easy Pro › Citations', url: '/footnotes-made-easy/pro-citations-styles', excerpt: 'APA 7th edition, MLA 9th edition, Chicago 17th edition Notes-Bibliography formatting rules and examples.' },
    { title: 'Footnote Library', section: 'Footnotes Made Easy Pro', url: '/footnotes-made-easy/pro-library', excerpt: 'Save footnotes once and reuse across posts. Search, import, export the Library.' },
    { title: 'Gutenberg Sidebar', section: 'Footnotes Made Easy Pro', url: '/footnotes-made-easy/pro-gutenberg-sidebar', excerpt: 'Manage footnotes from the block editor sidebar. Add, edit, delete, insert from Library, citation mode.' },
    { title: 'Pro — FAQ', section: 'Footnotes Made Easy Pro', url: '/footnotes-made-easy/pro-faq', excerpt: 'FAQ on licensing, citations, library, and Gutenberg sidebar for Footnotes Made Easy Pro.' },
    // Account
    { title: 'Managing Your License', section: 'Account', url: '/account/managing-your-license', excerpt: 'View, activate, deactivate, transfer, and renew your AltviseWP license from your account dashboard.' },
    { title: 'Billing and Renewals', section: 'Account', url: '/account/billing-and-renewals', excerpt: 'Payment methods (Stripe, PayPal), invoices, auto-renewal, cancellation, failed payments.' },
    { title: 'Refunds', section: 'Account', url: '/account/refunds', excerpt: '14-day money-back guarantee. How to request a refund, processing time, post-refund steps.' },
  ];

  // ── Search logic ─────────────────────────────────────────
  function searchDocs( query ) {
    if ( ! query || query.length < 2 ) return [];
    const q = query.toLowerCase().trim();
    const results = [];

    for ( const item of SEARCH_INDEX ) {
      const titleScore   = item.title.toLowerCase().includes( q ) ? 3 : 0;
      const sectionScore = item.section.toLowerCase().includes( q ) ? 2 : 0;
      const excerptScore = item.excerpt.toLowerCase().includes( q ) ? 1 : 0;
      const score = titleScore + sectionScore + excerptScore;

      if ( score > 0 ) {
        results.push( { ...item, score } );
      }
    }

    return results.sort( ( a, b ) => b.score - a.score ).slice( 0, 8 );
  }

  function highlight( text, query ) {
    const q = query.replace( /[.*+?^${}()|[\]\\]/g, '\\$&' );
    return text.replace( new RegExp( `(${q})`, 'gi' ), '<mark>$1</mark>' );
  }

  function renderResults( results, query, container ) {
    if ( results.length === 0 ) {
      container.innerHTML = `<div class="search-empty">No results for "<strong>${query}</strong>"</div>`;
      return;
    }
    container.innerHTML = results.map( ( r, i ) => `
      <a href="${r.url}" class="search-result${i === 0 ? ' selected' : ''}" data-index="${i}">
        <div class="search-result__title">${highlight( r.title, query )}</div>
        <div class="search-result__section">${r.section}</div>
        <div class="search-result__excerpt">${highlight( r.excerpt.substring( 0, 100 ) + '…', query )}</div>
      </a>
    ` ).join( '' );
  }

  // ── Search overlay ───────────────────────────────────────
  const overlay     = document.getElementById( 'search-overlay' );
  const modalInput  = document.getElementById( 'search-modal-input' );
  const resultsEl   = document.getElementById( 'search-results' );
  const closeBtn    = document.getElementById( 'search-close' );
  const topbarInput = document.getElementById( 'search-input' );

  let selectedIndex = 0;
  let currentResults = [];

  function openSearch() {
    overlay.classList.add( 'open' );
    modalInput.focus();
    document.body.style.overflow = 'hidden';
  }

  function closeSearch() {
    overlay.classList.remove( 'open' );
    modalInput.value = '';
    resultsEl.innerHTML = '';
    document.body.style.overflow = '';
    selectedIndex = 0;
  }

  topbarInput.addEventListener( 'click', openSearch );
  topbarInput.addEventListener( 'focus', openSearch );
  closeBtn.addEventListener( 'click', closeSearch );

  overlay.addEventListener( 'click', function ( e ) {
    if ( e.target === overlay ) closeSearch();
  } );

  modalInput.addEventListener( 'input', function () {
    const q = this.value.trim();
    currentResults = searchDocs( q );
    if ( q.length >= 2 ) {
      renderResults( currentResults, q, resultsEl );
      selectedIndex = 0;
    } else {
      resultsEl.innerHTML = '';
    }
  } );

  // Keyboard navigation
  document.addEventListener( 'keydown', function ( e ) {
    // Open with Cmd/Ctrl+K
    if ( ( e.metaKey || e.ctrlKey ) && e.key === 'k' ) {
      e.preventDefault();
      openSearch();
      return;
    }

    if ( ! overlay.classList.contains( 'open' ) ) return;

    if ( e.key === 'Escape' ) { closeSearch(); return; }

    const items = resultsEl.querySelectorAll( '.search-result' );
    if ( ! items.length ) return;

    if ( e.key === 'ArrowDown' ) {
      e.preventDefault();
      items[ selectedIndex ]?.classList.remove( 'selected' );
      selectedIndex = Math.min( selectedIndex + 1, items.length - 1 );
      items[ selectedIndex ]?.classList.add( 'selected' );
      items[ selectedIndex ]?.scrollIntoView( { block: 'nearest' } );
    } else if ( e.key === 'ArrowUp' ) {
      e.preventDefault();
      items[ selectedIndex ]?.classList.remove( 'selected' );
      selectedIndex = Math.max( selectedIndex - 1, 0 );
      items[ selectedIndex ]?.classList.add( 'selected' );
      items[ selectedIndex ]?.scrollIntoView( { block: 'nearest' } );
    } else if ( e.key === 'Enter' ) {
      e.preventDefault();
      items[ selectedIndex ]?.click();
    }
  } );

  // ── Theme toggle ─────────────────────────────────────────
  var html        = document.documentElement;
  var themeToggle = document.getElementById( 'theme-toggle' );
  var saved       = localStorage.getItem( 'apu-theme' );

  // Apply saved preference, otherwise respect OS preference
  if ( saved === 'light' || saved === 'dark' ) {
    html.setAttribute( 'data-theme', saved );
  } else if ( window.matchMedia( '(prefers-color-scheme: light)' ).matches ) {
    html.setAttribute( 'data-theme', 'light' );
  } else {
    html.setAttribute( 'data-theme', 'dark' );
  }

  if ( themeToggle ) {
    themeToggle.addEventListener( 'click', function () {
      var current = html.getAttribute( 'data-theme' );
      var next    = current === 'dark' ? 'light' : 'dark';
      html.setAttribute( 'data-theme', next );
      localStorage.setItem( 'apu-theme', next );
    } );
  }

  // ── Active nav link ───────────────────────────────────────
  const currentPath = window.location.pathname.replace( /\/$/, '' );
  document.querySelectorAll( '.sidenav__link' ).forEach( function ( link ) {
    const href = link.getAttribute( 'href' );
    if ( href && currentPath.endsWith( href.replace( '.html', '' ) ) ) {
      link.classList.add( 'active' );
    }
  } );

} )();
