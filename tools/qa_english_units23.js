// Keep the existing CI/local entry point; the shared runner derives totals from catalog.
process.argv.push('--units=2,3');
require('./qa_english_units.js');
