import sqlite3

def seed_all_ranks_data():
    conn = sqlite3.connect("marvel_rivals.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hero_rank_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hero_name TEXT,
            role TEXT,
            tier TEXT,
            win_rate REAL,
            pick_rate REAL,
            ban_rate REAL,
            rank_tier TEXT
        )
    """)
    
    cursor.execute("DELETE FROM hero_rank_stats")

    all_ranks_stats = [
        ("Peni Parker", "Vanguard", "S", 60.91, 7.54, 30.23, "All Ranks"),
        ("Ultron", "Strategist", "S", 57.07, 6.00, 0.16, "All Ranks"),
        ("Gorr The God Butcher", "Duelist", "S", 55.71, 8.30, 13.53, "All Ranks"),
        ("Rocket Raccoon", "Strategist", "S", 55.36, 14.04, 0.37, "All Ranks"),
        ("Storm", "Duelist", "A", 55.05, 5.04, 0.21, "All Ranks"),
        ("Magik", "Duelist", "S", 54.89, 7.57, 3.54, "All Ranks"),
        ("Mantis", "Strategist", "A", 54.54, 5.76, 0.10, "All Ranks"),
        ("Hulk", "Vanguard", "S", 54.19, 10.31, 0.93, "All Ranks"),
        ("Devil Dinosaur", "Vanguard", "S", 53.90, 13.04, 43.60, "All Ranks"),
        
        ("Mister Fantastic", "Duelist", "A", 53.33, 6.62, 0.39, "All Ranks"),
        ("Thor", "Vanguard", "A", 52.44, 9.33, 0.64, "All Ranks"),
        ("Daredevil", "Duelist", "A", 52.41, 6.17, 4.39, "All Ranks"),
        ("Captain America", "Vanguard", "A", 52.39, 5.44, 0.23, "All Ranks"),
        ("Doctor Strange", "Vanguard", "S", 51.55, 24.25, 0.95, "All Ranks"),
        ("Loki", "Strategist", "A", 51.50, 5.74, 0.75, "All Ranks"),
        ("Adam Warlock", "Strategist", "B", 51.35, 4.69, 0.20, "All Ranks"),
        ("Rogue", "Vanguard", "A", 50.93, 9.54, 0.63, "All Ranks"),
        ("Hela", "Duelist", "A", 50.82, 12.15, 6.17, "All Ranks"),

        ("Human Torch", "Duelist", "B", 50.68, 3.12, 0.46, "All Ranks"),
        ("Iron Fist", "Duelist", "B", 50.66, 6.84, 1.57, "All Ranks"),
        ("Angela", "Vanguard", "B", 50.53, 4.53, 0.60, "All Ranks"),
        ("Groot", "Vanguard", "B", 50.29, 5.06, 1.50, "All Ranks"),
        ("Iron Man", "Duelist", "B", 50.18, 5.98, 0.76, "All Ranks"),
        ("Psylocke", "Duelist", "B", 50.10, 7.46, 6.10, "All Ranks"),
        ("Scarlet Witch", "Duelist", "B", 50.05, 16.32, 5.75, "All Ranks"),
        ("Jubilee", "Strategist", "A", 49.93, 30.39, 1.95, "All Ranks"),
        ("Venom", "Vanguard", "B", 49.75, 8.87, 1.00, "All Ranks"),
        ("Invisible Woman", "Strategist", "B", 49.65, 27.09, 1.16, "All Ranks"),
        ("Blade", "Duelist", "B", 49.50, 5.29, 0.99, "All Ranks"),
        ("Spider-Man", "Duelist", "B", 49.03, 17.54, 18.22, "All Ranks"),
        ("The Hood", "Vanguard", "B", 48.88, 17.57, 1.39, "All Ranks"),
        ("Black Panther", "Duelist", "B", 48.81, 5.98, 7.75, "All Ranks"),
        ("White Fox", "Strategist", "B", 48.61, 16.27, 0.26, "All Ranks"),
        ("Emma Frost", "Vanguard", "B", 48.15, 20.78, 17.85, "All Ranks"),
        ("Gambit", "Strategist", "B", 47.92, 21.21, 16.32, "All Ranks"),
        ("Luna Snow", "Strategist", "B", 47.67, 23.53, 0.51, "All Ranks"),
        ("Winter Soldier", "Duelist", "B", 47.56, 19.01, 12.53, "All Ranks"),

        ("Wolverine", "Duelist", "C", 48.28, 4.45, 3.76, "All Ranks"),
        ("Black Cat", "Duelist", "C", 48.19, 3.96, 0.89, "All Ranks"),
        ("Star-Lord", "Duelist", "C", 47.91, 4.97, 0.27, "All Ranks"),
        ("Elsa Bloodstone", "Duelist", "C", 47.39, 7.96, 19.87, "All Ranks"),
        ("Magneto", "Vanguard", "C", 47.21, 20.55, 1.86, "All Ranks"),
        ("Hawkeye", "Duelist", "D", 47.09, 4.06, 0.32, "All Ranks"),
        ("Phoenix", "Duelist", "C", 47.03, 11.33, 35.16, "All Ranks"),
        ("The Thing", "Vanguard", "C", 46.90, 7.04, 2.21, "All Ranks"),
        ("Jeff The Land Shark", "Strategist", "C", 46.43, 14.58, 0.36, "All Ranks"),
        ("Namor", "Duelist", "C", 45.97, 12.80, 9.36, "All Ranks"),
        ("Moon Knight", "Duelist", "D", 45.54, 6.90, 0.85, "All Ranks"),
        ("Cloak & Dagger", "Strategist", "C", 45.31, 25.12, 5.26, "All Ranks"),
        ("Cyclops", "Duelist", "D", 44.95, 13.32, 2.07, "All Ranks"),
        ("Black Widow", "Duelist", "D", 44.82, 3.80, 0.25, "All Ranks"),
        ("The Punisher", "Duelist", "D", 44.09, 8.64, 1.14, "All Ranks"),
        ("Squirrel Girl", "Duelist", "D", 42.71, 5.53, 0.71, "All Ranks"),
        ("Deadpool", "Vanguard", "C", 48.10, 4.68, 0.36, "All Ranks"),
        ("Deadpool", "Strategist", "B", 48.34, 3.67, 0.48, "All Ranks"),
        ("Deadpool", "Duelist", "D", 47.54, 1.42, 0.32, "All Ranks")
    ]

    cursor.executemany("""
        INSERT INTO hero_rank_stats (hero_name, role, tier, win_rate, pick_rate, ban_rate, rank_tier)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, all_ranks_stats)

    conn.commit()
    conn.close()
    print("Database successfully seeded with tracker statistics")

if __name__ == "__main__":
    seed_all_ranks_data()
