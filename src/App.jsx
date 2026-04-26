import { useState, useMemo } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Search, Info, Crosshair, Settings, DollarSign, Activity, Target, Shield, Flame, Battery, BatteryCharging, PlugZap, ChevronDown, Zap, Calendar } from 'lucide-react';
import blastersData from './blasters_data.json';
import './index.css';

// Remove duplicates if any
const uniqueBlasters = blastersData.filter((b, index, self) => 
  index === self.findIndex(t => t.id === b.id)
);

function BlasterCard({ blaster }) {
  const [intelExpanded, setIntelExpanded] = useState(false);

  return (
    <motion.div
      layout
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.9 }}
      transition={{ duration: 0.4 }}
      className="glass-panel"
      style={{ overflow: 'hidden', display: 'flex', flexDirection: 'column', position: 'relative' }}
      whileHover={{ y: -5, boxShadow: '0 10px 30px -10px var(--accent-glow)', borderColor: 'rgba(0, 229, 255, 0.4)' }}
    >
      {blaster.in_stock !== false ? (
        <div style={{ position: 'absolute', top: '16px', right: '16px', background: 'rgba(0,0,0,0.6)', padding: '6px 12px', borderRadius: '20px', display: 'flex', alignItems: 'center', gap: '6px', backdropFilter: 'blur(8px)', zIndex: '10' }}>
          <Activity size={14} color="#2ed573" />
          <span style={{ fontSize: '0.8rem', fontWeight: '600', color: '#2ed573' }}>IN STOCK</span>
        </div>
      ) : (
        <div style={{ position: 'absolute', top: '16px', right: '16px', background: 'rgba(0,0,0,0.6)', padding: '6px 12px', borderRadius: '20px', display: 'flex', alignItems: 'center', gap: '6px', backdropFilter: 'blur(8px)', zIndex: '10' }}>
          <Target size={14} color="#e74c3c" />
          <span style={{ fontSize: '0.8rem', fontWeight: '600', color: '#e74c3c' }}>OUT OF STOCK</span>
        </div>
      )}

      <div style={{ height: '260px', overflow: 'hidden', position: 'relative', background: 'rgba(0,0,0,0.2)' }}>
        {blaster.image ? (
          <img 
            src={blaster.image} 
            alt={blaster.title} 
            style={{ width: '100%', height: '100%', objectFit: 'cover', filter: blaster.in_stock === false ? 'grayscale(100%) opacity(0.6)' : 'none' }}
          />
        ) : (
          <div style={{ width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-secondary)' }}>
            No Image Available
          </div>
        )}
        <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, height: '100px', background: 'linear-gradient(to top, rgba(22, 26, 31, 1), transparent)' }}></div>
      </div>

      <div style={{ padding: '1.5rem', flex: '1', display: 'flex', flexDirection: 'column' }}>
        <h3 style={{ fontSize: '1.3rem', fontWeight: '600', marginBottom: '1.5rem', lineHeight: '1.3' }}>
          {blaster.title}
        </h3>
        
        {/* Section 1: Performance Analytics */}
        <div style={{ marginBottom: '1.5rem' }}>
          <div style={{ fontSize: '0.7rem', color: 'var(--accent)', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.1em', marginBottom: '0.8rem', opacity: 0.8 }}>
            Performance Analytics
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.2rem' }}>
            {/* FPS Stat */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '10px' }}>
              <div style={{ background: 'rgba(0, 229, 255, 0.05)', padding: '8px', borderRadius: '8px', flexShrink: 0 }}><Target size={18} color="var(--accent)" /></div>
              <div style={{ minWidth: 0 }}>
                <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase' }}>Mech FPS</div>
                <div style={{ fontWeight: '600', fontSize: '0.9rem' }}>{blaster.fps}</div>
              </div>
            </div>
            
            {/* Voltage RPS Stat */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '10px' }}>
              <div style={{ background: 'rgba(255, 71, 87, 0.1)', padding: '8px', borderRadius: '8px', flexShrink: 0 }}><Flame size={18} color="var(--danger)" /></div>
              <div style={{ minWidth: 0 }}>
                <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase' }}>Rate of Fire</div>
                <div style={{ fontWeight: '600', fontSize: '0.9rem' }}>
                  {blaster.rps_7v === "N/A" || !blaster.rps_7v ? "N/A" : `${blaster.rps_11v} RPS`}
                </div>
              </div>
            </div>

            {/* Cheap Gels FPS */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '10px' }}>
              <div style={{ background: 'rgba(255,255,255,0.05)', padding: '8px', borderRadius: '8px', flexShrink: 0 }}><Zap size={18} color="#95a5a6" /></div>
              <div style={{ minWidth: 0 }}>
                <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase' }}>Cheap Gels</div>
                <div style={{ fontWeight: '500', fontSize: '0.85rem', color: '#95a5a6' }}>{blaster.cross_referenced_specs?.fps_cheap}</div>
              </div>
            </div>

            {/* Ultra Gels FPS */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '10px' }}>
              <div style={{ background: 'rgba(0, 229, 255, 0.1)', padding: '8px', borderRadius: '8px', flexShrink: 0 }}><Flame size={18} color="var(--accent)" /></div>
              <div style={{ minWidth: 0 }}>
                <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase' }}>Ultra-Hard</div>
                <div style={{ fontWeight: '700', fontSize: '0.9rem', color: 'var(--accent)' }}>{blaster.cross_referenced_specs?.fps_ultra}</div>
              </div>
            </div>
          </div>
        </div>

        {/* Section 2: Hardware Architecture */}
        <div style={{ marginBottom: '1.5rem' }}>
          <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', fontWeight: '700', textTransform: 'uppercase', letterSpacing: '0.1em', marginBottom: '0.8rem', opacity: 0.6 }}>
            Hardware Architecture
          </div>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.2rem' }}>
            {/* Gearbox Stat */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '10px' }}>
              <div style={{ background: 'rgba(255,255,255,0.05)', padding: '8px', borderRadius: '8px', flexShrink: 0 }}><Settings size={18} color="var(--text-secondary)" /></div>
              <div style={{ minWidth: 0 }}>
                <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase' }}>Gearbox</div>
                <div style={{ fontWeight: '500', fontSize: '0.8rem', lineHeight: '1.4' }}>{blaster.gearbox}</div>
              </div>
            </div>

            {/* Material Stat */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '10px' }}>
              <div style={{ background: 'rgba(255,255,255,0.05)', padding: '8px', borderRadius: '8px', flexShrink: 0 }}><Shield size={18} color="#ffa502" /></div>
              <div style={{ minWidth: 0 }}>
                <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase' }}>Body</div>
                <div style={{ fontWeight: '500', fontSize: '0.8rem', lineHeight: '1.4' }}>{blaster.cross_referenced_specs?.material}</div>
              </div>
            </div>

            {/* Release Date Stat */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '10px' }}>
              <div style={{ background: 'rgba(255,255,255,0.05)', padding: '8px', borderRadius: '8px', flexShrink: 0 }}><Calendar size={18} color="#a0aab5" /></div>
              <div style={{ minWidth: 0 }}>
                <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase' }}>Release</div>
                <div style={{ fontWeight: '500', fontSize: '0.85rem' }}>{blaster.release_date || 'N/A'}</div>
              </div>
            </div>

            {/* Terminal/Plug Stat */}
            <div style={{ display: 'flex', alignItems: 'flex-start', gap: '10px' }}>
              <div style={{ background: 'rgba(46, 213, 115, 0.1)', padding: '8px', borderRadius: '8px', flexShrink: 0 }}><PlugZap size={18} color="#2ed573" /></div>
              <div style={{ minWidth: 0 }}>
                <div style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase' }}>Plug</div>
                <div style={{ fontWeight: '600', fontSize: '0.85rem', color: '#2ed573' }}>{blaster.cross_referenced_specs?.battery}</div>
              </div>
            </div>
          </div>

          {/* Factory Spring Rating — only shown when specific teardown data exists */}
          {blaster.cross_referenced_specs?.factory_spring && (
            <div style={{ marginTop: '1.2rem', display: 'flex', alignItems: 'center', gap: '12px', padding: '0.8rem 1rem', background: 'rgba(255, 165, 2, 0.05)', border: '1px solid rgba(255, 165, 2, 0.2)', borderRadius: '10px' }}>
              <div style={{ background: 'rgba(255, 165, 2, 0.1)', padding: '8px', borderRadius: '8px', flexShrink: 0 }}>
                <Zap size={18} color="#ffa502" />
              </div>
              <div>
                <div style={{ fontSize: '0.7rem', color: '#ffa502', textTransform: 'uppercase', fontWeight: '700', letterSpacing: '0.08em' }}>Factory Spring (Teardown Confirmed)</div>
                <div style={{ fontWeight: '700', fontSize: '0.95rem', color: '#ffa502' }}>{blaster.cross_referenced_specs.factory_spring}</div>
              </div>
            </div>
          )}
        </div>

        <div style={{ flex: '1', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          
          {/* Collapsible Chinese Forum Intelligence */}
          {blaster.cross_referenced_specs && (
            <div style={{ background: 'rgba(0, 229, 255, 0.03)', borderLeft: '3px solid var(--accent)', borderRadius: '0 8px 8px 0', overflow: 'hidden' }}>
              <div 
                onClick={() => setIntelExpanded(!intelExpanded)}
                style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '0.8rem 1rem', cursor: 'pointer', userSelect: 'none' }}
              >
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                  <Info size={16} color="var(--accent)" />
                  <span style={{ fontSize: '0.85rem', fontWeight: '600', color: 'var(--accent)' }}>
                    Mainland Technical Intelligence Repository
                  </span>
                </div>
                <motion.div animate={{ rotate: intelExpanded ? 180 : 0 }}>
                  <ChevronDown size={18} color="var(--accent)" />
                </motion.div>
              </div>

              <AnimatePresence>
                {intelExpanded && (
                  <motion.div 
                    initial={{ height: 0, opacity: 0 }}
                    animate={{ height: 'auto', opacity: 1 }}
                    exit={{ height: 0, opacity: 0 }}
                    style={{ overflow: 'hidden' }}
                  >
                    <div style={{ padding: '0 1rem 1rem 1rem' }}>
                      <p style={{ fontSize: '0.85rem', color: 'rgba(255,255,255,0.85)', lineHeight: '1.5', fontWeight: '400' }}>
                        {blaster.cross_referenced_specs.notes.split('\n').map((line, i) => {
                          const isWarning = line.includes('TECH WARNING:');
                          const parts = line.split('**');
                          
                          // If it's the combined paragraph and has a warning, we can highlight the warning part
                          // but the split mapping is fine.
                          return (
                            <span key={i} style={{ display: 'block', marginBottom: '8px', color: 'var(--text-secondary)' }}>
                              {parts.map((part, index) => 
                                index % 2 === 1 ? <strong key={index} style={{ color: 'var(--accent)', fontWeight: '700' }}>{part}</strong> : 
                                (part.includes('TECH WARNING:') ? 
                                  <span key={index}>
                                    {part.split('TECH WARNING:')[0]}
                                    <strong style={{ color: '#ff6b6b', fontWeight: '700' }}>TECH WARNING:</strong>
                                    <span style={{ color: '#ff6b6b' }}>{part.split('TECH WARNING:')[1]}</span>
                                  </span>
                                : part)
                              )}
                            </span>
                          );
                        })}
                      </p>
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          )}


        </div>

        <div style={{ marginTop: '1.5rem', paddingTop: '1.5rem', borderTop: '1px solid var(--panel-border)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '4px' }}>
            <DollarSign size={24} color="var(--accent)" style={{ transition: '0.3s' }} />
            <span style={{ fontSize: '1.8rem', fontWeight: '700', color: 'var(--text-primary)' }}>
              {blaster.price.toFixed(2)}
            </span>
          </div>
          <a 
            href={blaster.url} 
            target="_blank" 
            rel="noreferrer"
            style={{ 
              display: 'inline-flex', padding: '0.8rem 1.5rem', background: 'rgba(0, 229, 255, 0.1)', 
              color: 'var(--accent)', borderRadius: '8px', textDecoration: 'none', 
              fontWeight: '600', transition: 'all 0.3s', border: '1px solid var(--accent)'
            }}
            onMouseEnter={(e) => { e.target.style.background = 'var(--accent)'; e.target.style.color = '#000'; }}
            onMouseLeave={(e) => { e.target.style.background = 'rgba(0, 229, 255, 0.1)'; e.target.style.color = 'var(--accent)'; }}
          >
            View Retail Page
          </a>
        </div>
      </div>
    </motion.div>
  );
}

export default function App() {
  const [searchTerm, setSearchTerm] = useState('');
  const [sortBy, setSortBy] = useState('release-desc');
  
  const [filterMaterial, setFilterMaterial] = useState('All');
  const [filterConnector, setFilterConnector] = useState('All');
  const [filterYear, setFilterYear] = useState('All');
  const [filterCategory, setFilterCategory] = useState('All');
  const [filterStock, setFilterStock] = useState('In Stock Only');
  
  const filteredAndSortedBlasters = useMemo(() => {
    let result = uniqueBlasters.filter(b => {
      const sTerm = searchTerm.toLowerCase();
      const stringified = JSON.stringify(b).toLowerCase();
      
      const mat = (b.cross_referenced_specs?.material || '').toLowerCase();
      const conn = (b.cross_referenced_specs?.battery || '').toLowerCase();
      const cat = (b.category || '').toLowerCase();
      
      if (sTerm && !stringified.includes(sTerm)) return false;
      
      if (filterStock === 'In Stock Only' && b.in_stock === false) return false;
      if (filterStock === 'Out of Stock Only' && b.in_stock !== false) return false;
      
      if (filterCategory !== 'All' && cat !== filterCategory.toLowerCase()) return false;
      if (filterMaterial !== 'All' && !mat.includes(filterMaterial.toLowerCase())) return false;
      if (filterConnector !== 'All' && !conn.includes(filterConnector.toLowerCase())) return false;
      
      if (filterYear !== 'All') {
        const year = b.release_date ? b.release_date.split('-')[0] : '';
        if (year !== filterYear) return false;
      }
      
      return true;
    });
    
    result.sort((a, b) => {
      if (sortBy === 'price-asc') return a.price - b.price;
      if (sortBy === 'price-desc') return b.price - a.price;
      if (sortBy === 'release-desc') return (b.release_timestamp || 0) - (a.release_timestamp || 0);
      if (sortBy === 'release-asc') return (a.release_timestamp || 0) - (b.release_timestamp || 0);
      if (sortBy === 'name') return a.title.localeCompare(b.title);
      if (sortBy === 'fps-desc') return (b.fps_num || 0) - (a.fps_num || 0);
      if (sortBy === 'fps-asc') return (a.fps_num || 0) - (b.fps_num || 0);
      if (sortBy === 'rps-desc') return (b.rps_11v || 0) - (a.rps_11v || 0);
      if (sortBy === 'rps-asc') return (a.rps_11v || 0) - (b.rps_11v || 0);
      return 0;
    });
    
    return result;
  }, [searchTerm, sortBy, filterMaterial, filterConnector, filterYear, filterCategory, filterStock]);

  return (
    <div style={{ width: '100%', minHeight: '100vh' }}>
      
      {/* Header — full width strip */}
      <motion.header 
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        style={{ padding: '2rem 2.5rem 1.5rem', borderBottom: '1px solid var(--panel-border)', display: 'flex', alignItems: 'center', gap: '1.5rem', flexWrap: 'wrap' }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', flex: '1', minWidth: '280px' }}>
          <Crosshair size={40} color="var(--accent)" />
          <div>
            <h1 style={{ fontSize: '2rem', fontWeight: '700', letterSpacing: '-0.02em', background: 'linear-gradient(135deg, #fff, #a0aab5)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent', lineHeight: 1.2 }}>
              Tactical Arsenal Tracker
            </h1>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', lineHeight: '1.5', marginTop: '4px' }}>
              AKGelBlaster Intel — cross-referenced Chinese forum teardowns &amp; live stock data.
            </p>
          </div>
        </div>
        {/* Result count badge */}
        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '0.5rem 1rem', background: 'rgba(0,229,255,0.05)', border: '1px solid rgba(0,229,255,0.2)', borderRadius: '20px' }}>
          <Activity size={14} color="var(--accent)" />
          <span style={{ fontSize: '0.85rem', color: 'var(--accent)', fontWeight: '600' }}>{filteredAndSortedBlasters.length} <span style={{ color: 'var(--text-secondary)', fontWeight: '400' }}>platforms indexed</span></span>
        </div>
      </motion.header>

      {/* Body — Sidebar + Content two-column layout */}
      <div style={{ display: 'flex', alignItems: 'flex-start', width: '100%' }}>

        {/* ── Left Sidebar: Filters ── */}
        <motion.aside
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.6, delay: 0.1 }}
          style={{
            width: '260px',
            flexShrink: 0,
            position: 'sticky',
            top: 0,
            height: '100vh',
            overflowY: 'auto',
            borderRight: '1px solid var(--panel-border)',
            padding: '1.5rem 1.2rem',
            display: 'flex',
            flexDirection: 'column',
            gap: '1.4rem',
            background: 'rgba(13,15,18,0.95)',
            backdropFilter: 'blur(16px)',
            scrollbarWidth: 'thin',
          }}
        >
          {/* Search */}
          <div style={{ position: 'relative' }}>
            <Search size={16} color="var(--accent)" style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', opacity: 0.7 }} />
            <input
              type="text"
              placeholder="Search arsenal..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              style={{
                width: '100%', padding: '0.75rem 0.75rem 0.75rem 2.4rem',
                background: 'rgba(0,0,0,0.5)', border: '1px solid var(--panel-border)',
                borderRadius: '10px', color: 'var(--text-primary)', fontSize: '0.9rem',
                outline: 'none', transition: 'all 0.3s',
              }}
              onFocus={(e) => { e.target.style.borderColor = 'var(--accent)'; e.target.style.boxShadow = '0 0 10px var(--accent-glow)'; }}
              onBlur={(e) => { e.target.style.borderColor = 'var(--panel-border)'; e.target.style.boxShadow = 'none'; }}
            />
          </div>

          <div style={{ borderTop: '1px solid var(--panel-border)', paddingTop: '1rem' }}>
            <div style={{ fontSize: '0.65rem', color: 'var(--accent)', fontWeight: '800', textTransform: 'uppercase', letterSpacing: '0.12em', marginBottom: '1rem' }}>Filters</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1.1rem' }}>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <label style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase', fontWeight: '600', letterSpacing: '0.06em' }}>Deployment</label>
                <select value={filterStock} onChange={(e) => setFilterStock(e.target.value)}
                  style={{ width: '100%', padding: '0.6rem 0.8rem', background: 'rgba(255,255,255,0.03)', border: '1px solid var(--panel-border)', borderRadius: '8px', color: 'var(--text-primary)', outline: 'none', cursor: 'pointer', fontSize: '0.85rem' }}>
                  <option value="In Stock Only">In Stock Only</option>
                  <option value="Out of Stock Only">Out of Stock Only</option>
                  <option value="All">All Inventory</option>
                </select>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <label style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase', fontWeight: '600', letterSpacing: '0.06em' }}>Category</label>
                <select value={filterCategory} onChange={(e) => setFilterCategory(e.target.value)}
                  style={{ width: '100%', padding: '0.6rem 0.8rem', background: 'rgba(255,255,255,0.03)', border: '1px solid var(--panel-border)', borderRadius: '8px', color: 'var(--text-primary)', outline: 'none', cursor: 'pointer', fontSize: '0.85rem' }}>
                  <option value="All">All Categories</option>
                  <option value="Rifle">Assault Rifles</option>
                  <option value="SMG">SMG / PDW</option>
                  <option value="Pistol">Sidearms / EBB</option>
                </select>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <label style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase', fontWeight: '600', letterSpacing: '0.06em' }}>Material</label>
                <select value={filterMaterial} onChange={(e) => setFilterMaterial(e.target.value)}
                  style={{ width: '100%', padding: '0.6rem 0.8rem', background: 'rgba(255,255,255,0.03)', border: '1px solid var(--panel-border)', borderRadius: '8px', color: 'var(--text-primary)', outline: 'none', cursor: 'pointer', fontSize: '0.85rem' }}>
                  <option value="All">Any Material</option>
                  <option value="Metal">Full Metal / Alloy</option>
                  <option value="Nylon">High-Grade Nylon</option>
                  <option value="Steel">Stamped Steel</option>
                </select>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <label style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase', fontWeight: '600', letterSpacing: '0.06em' }}>Connector</label>
                <select value={filterConnector} onChange={(e) => setFilterConnector(e.target.value)}
                  style={{ width: '100%', padding: '0.6rem 0.8rem', background: 'rgba(255,255,255,0.03)', border: '1px solid var(--panel-border)', borderRadius: '8px', color: 'var(--text-primary)', outline: 'none', cursor: 'pointer', fontSize: '0.85rem' }}>
                  <option value="All">All Connectors</option>
                  <option value="XT30">XT30 (Modern)</option>
                  <option value="Deans">Deans (T-Plug)</option>
                  <option value="Tamiya">Mini Tamiya</option>
                  <option value="SM">SM Plug</option>
                </select>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '6px' }}>
                <label style={{ fontSize: '0.7rem', color: 'var(--text-secondary)', textTransform: 'uppercase', fontWeight: '600', letterSpacing: '0.06em' }}>Era</label>
                <select value={filterYear} onChange={(e) => setFilterYear(e.target.value)}
                  style={{ width: '100%', padding: '0.6rem 0.8rem', background: 'rgba(255,255,255,0.03)', border: '1px solid var(--panel-border)', borderRadius: '8px', color: 'var(--text-primary)', outline: 'none', cursor: 'pointer', fontSize: '0.85rem' }}>
                  <option value="All">All Years</option>
                  <option value="2026">2026 Season</option>
                  <option value="2025">2025 Season</option>
                  <option value="2024">2024 Season</option>
                  <option value="2023">2023 Season</option>
                </select>
              </div>

            </div>
          </div>

          <div style={{ borderTop: '1px solid var(--panel-border)', paddingTop: '1rem' }}>
            <div style={{ fontSize: '0.65rem', color: 'var(--accent)', fontWeight: '800', textTransform: 'uppercase', letterSpacing: '0.12em', marginBottom: '0.8rem' }}>Sort Priority</div>
            <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}
              className="tactical-accent-border glow-on-hover"
              style={{ width: '100%', padding: '0.6rem 0.8rem', background: 'rgba(0,229,255,0.04)', border: '1px solid var(--accent)', borderRadius: '8px', color: 'var(--accent)', outline: 'none', cursor: 'pointer', fontWeight: '600', fontSize: '0.85rem' }}>
              <option value="release-desc">Newest First</option>
              <option value="fps-desc">Max FPS</option>
              <option value="rps-desc">Max RPS</option>
              <option value="price-asc">Price: Low to High</option>
              <option value="price-desc">Price: High to Low</option>
              <option value="name">A - Z</option>
            </select>
          </div>

          {/* Reset button */}
          <button
            onClick={() => { setSearchTerm(''); setFilterStock('In Stock Only'); setFilterCategory('All'); setFilterMaterial('All'); setFilterConnector('All'); setFilterYear('All'); setSortBy('release-desc'); }}
            style={{ marginTop: 'auto', padding: '0.7rem', background: 'transparent', border: '1px solid var(--panel-border)', borderRadius: '8px', color: 'var(--text-secondary)', cursor: 'pointer', fontSize: '0.8rem', transition: 'all 0.2s', letterSpacing: '0.04em' }}
            onMouseEnter={(e) => { e.target.style.borderColor = 'var(--danger)'; e.target.style.color = 'var(--danger)'; }}
            onMouseLeave={(e) => { e.target.style.borderColor = 'var(--panel-border)'; e.target.style.color = 'var(--text-secondary)'; }}
          >
            Reset All Filters
          </button>
        </motion.aside>

        {/* ── Right: Card Grid ── */}
        <div style={{ flex: 1, minWidth: 0, padding: '1.5rem 1.5rem 2rem', overflowY: 'auto' }}>
          {/* Grid */}
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(min(100%, 300px), 1fr))', gap: '1.5rem' }}>
            <AnimatePresence>
              {filteredAndSortedBlasters.map((blaster) => (
                <BlasterCard key={blaster.id} blaster={blaster} />
              ))}
            </AnimatePresence>
          </div>

          {filteredAndSortedBlasters.length === 0 && (
            <div style={{ textAlign: 'center', padding: '4rem', color: 'var(--text-secondary)' }}>
              <Target size={48} style={{ opacity: 0.5, margin: '0 auto 1rem' }} />
              <h3>No intelligence found matching these filters.</h3>
            </div>
          )}
        </div>

      </div>
    </div>
  );
}
