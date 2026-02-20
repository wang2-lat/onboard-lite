from jinja2 import Template

def generate_code(tour_data: dict):
    """Generate embeddable HTML/JS code"""
    template_str = """<script>
(function() {
  const tourData = {{ tour_json }};
  let currentStep = 0;
  
  const styles = `
    .onboard-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9998; }
    .onboard-tooltip { position: absolute; background: white; border-radius: 8px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); z-index: 9999; max-width: 300px; }
    .onboard-title { font-size: 18px; font-weight: bold; margin-bottom: 10px; }
    .onboard-content { font-size: 14px; margin-bottom: 15px; color: #555; }
    .onboard-footer { display: flex; justify-content: space-between; align-items: center; }
    .onboard-btn { padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer; font-size: 14px; }
    .onboard-next { background: #007bff; color: white; }
    .onboard-skip { background: transparent; color: #666; }
  `;
  
  function init() {
    const styleEl = document.createElement('style');
    styleEl.textContent = styles;
    document.head.appendChild(styleEl);
    showStep(0);
  }
  
  function showStep(index) {
    if (index >= tourData.steps.length) {
      cleanup();
      return;
    }
    
    const step = tourData.steps[index];
    const target = document.querySelector(step.target);
    
    if (!target) {
      currentStep++;
      showStep(currentStep);
      return;
    }
    
    const overlay = document.createElement('div');
    overlay.className = 'onboard-overlay';
    overlay.onclick = () => { currentStep++; cleanup(); showStep(currentStep); };
    
    const tooltip = document.createElement('div');
    tooltip.className = 'onboard-tooltip';
    tooltip.innerHTML = `
      <div class="onboard-title">${step.title}</div>
      <div class="onboard-content">${step.content}</div>
      <div class="onboard-footer">
        <button class="onboard-btn onboard-skip">Skip</button>
        <span style="color: #999;">${index + 1}/${tourData.steps.length}</span>
        <button class="onboard-btn onboard-next">${index === tourData.steps.length - 1 ? 'Done' : 'Next'}</button>
      </div>
    `;
    
    document.body.appendChild(overlay);
    document.body.appendChild(tooltip);
    
    const rect = target.getBoundingClientRect();
    const positions = {
      bottom: { top: rect.bottom + 10, left: rect.left },
      top: { top: rect.top - tooltip.offsetHeight - 10, left: rect.left },
      left: { top: rect.top, left: rect.left - tooltip.offsetWidth - 10 },
      right: { top: rect.top, left: rect.right + 10 }
    };
    
    const pos = positions[step.position] || positions.bottom;
    tooltip.style.top = pos.top + 'px';
    tooltip.style.left = pos.left + 'px';
    
    tooltip.querySelector('.onboard-next').onclick = () => { currentStep++; cleanup(); showStep(currentStep); };
    tooltip.querySelector('.onboard-skip').onclick = () => cleanup();
  }
  
  function cleanup() {
    document.querySelectorAll('.onboard-overlay, .onboard-tooltip').forEach(el => el.remove());
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>"""
    
    import json
    tour_json = json.dumps(tour_data.get("tour", {}), indent=2)
    
    template = Template(template_str)
    return template.render(tour_json=tour_json)
