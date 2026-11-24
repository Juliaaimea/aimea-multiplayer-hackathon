/* @bruin
name: mart.team_summary
type: duckdb.sql
materialization:
  type: table
depends:
  - raw.interviews
@bruin */

SELECT
  role,
  COUNT(*) AS interviews,
  ROUND(AVG(minutes), 1) AS avg_minutes,
  ROUND(AVG(score_communication), 2) AS avg_communication,
  ROUND(AVG(score_problem_solving), 2) AS avg_problem_solving,
  SUM(CASE WHEN recommendation = 'advance' THEN 1 ELSE 0 END) AS advanced
FROM raw.interviews
GROUP BY role
ORDER BY role;
