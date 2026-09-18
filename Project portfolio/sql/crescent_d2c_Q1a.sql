-- Q1 — Funnel & Segment Diagnosis
-- At which funnel stage (Landing → PLP → PDP → Cart → Checkout) is drop-off highest, 
-- and does the pattern differ between new vs. returning visitors?

WITH FunnelStages AS (
    -- Mapped to the exact strings generated in your funnel_events table
    SELECT 'landing' AS stage_name, 1 AS stage_rank UNION ALL
    SELECT 'category', 2 UNION ALL  -- Matches the PLP stage in your CSV
    SELECT 'product', 3 UNION ALL   -- Matches the PDP stage in your CSV
    SELECT 'cart', 4 UNION ALL
    SELECT 'checkout', 5
),

SegmentedVolumes AS (
    -- Joins across your confirmed users, sessions, and funnel_events tables
    SELECT 
        u.is_returning,
        LOWER(f.stage) AS normalized_stage,
        fs.stage_rank,
        COUNT(DISTINCT f.session_id) AS traffic_volume
    FROM funnel_events f
    JOIN sessions s ON f.session_id = s.session_id
    JOIN users u ON s.user_id = u.user_id
    -- Forces lowercase matching so 'Category', 'Product', and 'Cart' align perfectly
    JOIN FunnelStages fs ON LOWER(f.stage) = fs.stage_name
    GROUP BY 
        u.is_returning, 
        LOWER(f.stage), 
        fs.stage_rank
),

DropoffCalculation AS (
    -- Evaluates the traffic from the preceding funnel stage
    SELECT 
        is_returning,
        normalized_stage AS stage,
        stage_rank,
        traffic_volume AS current_volume,
        LAG(traffic_volume) OVER (PARTITION BY is_returning ORDER BY stage_rank) AS previous_volume
    FROM SegmentedVolumes
)

-- Calculates absolute user loss and drop-off percentage
SELECT 
    CASE WHEN is_returning = 1 THEN 'Returning User' ELSE 'New User' END AS user_segment,
    stage,
    current_volume,
    previous_volume,
    (previous_volume - current_volume) AS users_lost,
    ROUND(100.0 * (previous_volume - current_volume) / previous_volume, 2) AS dropoff_percentage
FROM DropoffCalculation
ORDER BY is_returning, stage_rank;