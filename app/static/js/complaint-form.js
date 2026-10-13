'use strict';
(() => {
  const prior = document.getElementById('previous_report');
  const followLabel = document.getElementById('followup_label');
  const followDetails = document.getElementById('follow_up_details');
  if (!prior || !followLabel || !followDetails) return;
  const toggleFollowup = () => {
    const show = prior.value === 'yes';
    followLabel.hidden = !show;
    followDetails.required = show;
  };
  prior.addEventListener('change', toggleFollowup);
  toggleFollowup();
})();
