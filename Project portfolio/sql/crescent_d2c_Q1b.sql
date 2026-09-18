-- Epic 2, Task 9: Self-Join Cohort Query
-- Comparing New vs. Returning user funnel volumes side-by-side

WITH CohortVolumes AS (
    -- Base CTE aggregating traffic volume by stage and user type
    SELECT 
        u.is_returning,
        LOWER(f.stage) AS stage_name,
        COUNT(DISTINCT f.session_id) AS volume
    FROM funnel_events f
    JOIN sessions s ON f.session_id = s.session_id
    JOIN users u ON s.user_id = u.user_id
    GROUP BY u.is_returning, LOWER(f.stage)
)

-- The Self-Join: Joining the CohortVolumes CTE to itself
-- to pivot the New Users (0) and Returning Users (1) into side-by-side columns
SELECT 
    new_users.stage_name AS funnel_stage,
    new_users.volume AS new_user_traffic,
    returning_users.volume AS returning_user_traffic,
    -- Calculating the ratio of returning to new users at each stage
    ROUND((returning_users.volume * 100.0) / new_users.volume, 2) AS returning_to_new_ratio_pct
FROM CohortVolumes AS new_users
JOIN CohortVolumes AS returning_users 
    ON new_users.stage_name = returning_users.stage_name
WHERE new_users.is_returning = 0 
  AND returning_users.is_returning = 1
ORDER BY 
    CASE new_users.stage_name
        WHEN 'landing' THEN 1
        WHEN 'category' THEN 2
        WHEN 'product' THEN 3
        WHEN 'cart' THEN 4
        WHEN 'checkout' THEN 5
    END;