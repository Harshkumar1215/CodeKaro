/**
 * CODEKARO — Serverless Global Counter Endpoint
 * Handles atomic increment and read operations securely on serverless hosting platforms.
 */

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  const COUNTER_API_BASE = 'https://api.counterapi.dev/v1/codekaro_practice_edu_global/students_count';

  try {
    if (req.query.action === 'up' || req.method === 'POST') {
      const response = await fetch(`${COUNTER_API_BASE}/up`);
      const data = await response.json();
      return res.status(200).json({ students: data.count || data.value || 1 });
    } else {
      const response = await fetch(COUNTER_API_BASE);
      const data = await response.json();
      return res.status(200).json({ students: data.count || data.value || 0 });
    }
  } catch (error) {
    return res.status(500).json({ error: 'Unable to connect to global counter service' });
  }
}
