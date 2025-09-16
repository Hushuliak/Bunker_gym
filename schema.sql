CREATE TABLE IF NOT EXISTS members (
    id SERIAL PRIMARY KEY,
    last_name TEXT NOT NULL,
    first_name TEXT NOT NULL,
    phone TEXT,
    card_number TEXT UNIQUE,
    comment TEXT,
    renewal_date DATE,
    expiry_date DATE
);