SELECT 
    hero_name,
    role,
    tier,
    win_rate,
    pick_rate,
    ban_rate
FROM hero_rank_stats
ORDER BY win_rate DESC;

SELECT 
    hero_name,
    role,
    win_rate,
    pick_rate,
    DENSE_RANK() OVER (PARTITION BY role ORDER BY win_rate DESC) AS role_rank
FROM hero_rank_stats;

SELECT 
    role,
    COUNT(*) AS total_heroes,
    ROUND(AVG(win_rate), 2) AS avg_win_rate,
    ROUND(AVG(pick_rate), 2) AS avg_pick_rate,
    ROUND(AVG(ban_rate), 2) AS avg_ban_rate
FROM hero_rank_stats
GROUP BY role
ORDER BY avg_win_rate DESC;

SELECT 
    hero_name,
    role,
    ban_rate,
    win_rate
FROM hero_rank_stats
WHERE ban_rate > 10.0
ORDER BY ban_rate DESC;