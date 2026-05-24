import asyncio
from app.database import AsyncSessionLocal
from app.models.sections import Section, Square

SECTIONS = [
    {
        "id": "A",
        "name": "Tropical Section",
        "greenhouse_id": 1,
        "is_indoor": True,
        "center_x": -137.345,
        "center_y": 13.048,
        "entry_x": -142.000,
        "entry_y": 12.226
    },
    {
        "id": "B",
        "name": "Sub Tropical Section",
        "greenhouse_id": 1,
        "is_indoor": True,
        "center_x": -128.153,
        "center_y": 8.881,
        "entry_x": -130.650,
        "entry_y": 10.612
    },
    {
        "id": "D",
        "name": "Mediterranean Section",
        "greenhouse_id": 2,
        "is_indoor": True,
        "center_x": -158.208,
        "center_y": -1.851,
        "entry_x": -154.360,
        "entry_y": 2.805
    },
    {
        "id": "E",
        "name": "Temperate Climate Section",
        "greenhouse_id": 2,
        "is_indoor": True,
        "center_x": -163.483,
        "center_y": -7.163,
        "entry_x": -161.400,
        "entry_y": -5.985
    },
    {
        "id": "F",
        "name": "Succulents and Xerophytes",
        "greenhouse_id": 2,
        "is_indoor": True,
        "center_x": -155.997,
        "center_y": -8.168,
        "entry_x": -152.603,
        "entry_y": -5.250
    }
]

SQUARES = [
    # Section A — Tropical (17 declared, A3 has two physical squares)
    {"id": "A-1",  "section_id": "A", "square_number": 1,  "label": "A1",  "is_active": True,  "x": -142.000, "y": 12.226},
    {"id": "A-2",  "section_id": "A", "square_number": 2,  "label": "A2",  "is_active": True,  "x": -139.549, "y": 16.513},
    {"id": "A-3",  "section_id": "A", "square_number": 3,  "label": "A3",  "is_active": True,  "x": -133.239, "y": 21.837},
    {"id": "A-3B", "section_id": "A", "square_number": 3,  "label": "A3",  "is_active": True,  "x": -127.743, "y": 21.872},
    {"id": "A-4",  "section_id": "A", "square_number": 4,  "label": "A4",  "is_active": True,  "x": -124.180, "y": 18.376},
    {"id": "A-5",  "section_id": "A", "square_number": 5,  "label": "A5",  "is_active": True,  "x": -125.560, "y": 14.620},
    {"id": "A-6",  "section_id": "A", "square_number": 6,  "label": "A6",  "is_active": True,  "x": -129.510, "y": 14.172},
    {"id": "A-7",  "section_id": "A", "square_number": 7,  "label": "A7",  "is_active": True,  "x": -128.298, "y": 18.380},
    {"id": "A-8",  "section_id": "A", "square_number": 8,  "label": "A8",  "is_active": True,  "x": -134.000, "y": 19.026},
    {"id": "A-9",  "section_id": "A", "square_number": 9,  "label": "A9",  "is_active": True,  "x": -133.090, "y": 16.733},
    {"id": "A-10", "section_id": "A", "square_number": 10, "label": "A10", "is_active": True,  "x": -135.518, "y": 15.476},
    {"id": "A-11", "section_id": "A", "square_number": 11, "label": "A11", "is_active": True,  "x": -134.268, "y": 13.991},
    {"id": "A-12", "section_id": "A", "square_number": 12, "label": "A12", "is_active": True,  "x": -138.679, "y": 11.764},
    {"id": "A-13", "section_id": "A", "square_number": 13, "label": "A13", "is_active": True,  "x": -138.818, "y": 8.726},
    {"id": "A-14", "section_id": "A", "square_number": 14, "label": "A14", "is_active": True,  "x": -134.418, "y": 9.926},
    {"id": "A-15", "section_id": "A", "square_number": 15, "label": "A15", "is_active": True,  "x": -134.868, "y": 5.826},
    {"id": "A-16", "section_id": "A", "square_number": 16, "label": "A16", "is_active": True,  "x": -138.087, "y": 4.426},
    {"id": "A-17", "section_id": "A", "square_number": 17, "label": "A17", "is_active": True,  "x": -141.942, "y": 5.999},

    # Section B — Sub Tropical (6 squares)
    {"id": "B-1", "section_id": "B", "square_number": 1, "label": "B1", "is_active": True, "x": -130.650, "y": 10.612},
    {"id": "B-2", "section_id": "B", "square_number": 2, "label": "B2", "is_active": True, "x": -125.200, "y": 11.726},
    {"id": "B-3", "section_id": "B", "square_number": 3, "label": "B3", "is_active": True, "x": -124.173, "y": 7.826},
    {"id": "B-4", "section_id": "B", "square_number": 4, "label": "B4", "is_active": True, "x": -127.625, "y": 4.426},
    {"id": "B-5", "section_id": "B", "square_number": 5, "label": "B5", "is_active": True, "x": -131.350, "y": 5.576},
    {"id": "B-6", "section_id": "B", "square_number": 6, "label": "B6", "is_active": True, "x": -127.885, "y": 7.376},

    # Section D — Mediterranean (10 squares)
    {"id": "D-1",  "section_id": "D", "square_number": 1,  "label": "D1",  "is_active": True, "x": -154.360, "y": 2.805},
    {"id": "D-2",  "section_id": "D", "square_number": 2,  "label": "D2",  "is_active": True, "x": -152.098, "y": -0.545},
    {"id": "D-3",  "section_id": "D", "square_number": 3,  "label": "D3",  "is_active": True, "x": -153.960, "y": -4.151},
    {"id": "D-4",  "section_id": "D", "square_number": 4,  "label": "D4",  "is_active": True, "x": -158.020, "y": -3.425},
    {"id": "D-5",  "section_id": "D", "square_number": 5,  "label": "D5",  "is_active": True, "x": -155.891, "y": -0.433},
    {"id": "D-6",  "section_id": "D", "square_number": 6,  "label": "D6",  "is_active": True, "x": -161.724, "y": -3.971},
    {"id": "D-7",  "section_id": "D", "square_number": 7,  "label": "D7",  "is_active": True, "x": -167.197, "y": -4.135},
    {"id": "D-8",  "section_id": "D", "square_number": 8,  "label": "D8",  "is_active": True, "x": -162.824, "y": -0.273},
    {"id": "D-9",  "section_id": "D", "square_number": 9,  "label": "D9",  "is_active": True, "x": -161.770, "y": -0.385},
    {"id": "D-10", "section_id": "D", "square_number": 10, "label": "D10", "is_active": True, "x": -165.393, "y": 2.688},

    # Section E — Temperate Climate (7 declared, E3 decommissioned)
    {"id": "E-1", "section_id": "E", "square_number": 1, "label": "E1", "is_active": True,  "x": -161.400, "y": -5.985},
    {"id": "E-2", "section_id": "E", "square_number": 2, "label": "E2", "is_active": True,  "x": -163.939, "y": -8.535},
    {"id": "E-3", "section_id": "E", "square_number": 3, "label": "E3", "is_active": False, "x": -164.403, "y": -8.103},
    {"id": "E-4", "section_id": "E", "square_number": 4, "label": "E4", "is_active": True,  "x": -160.164, "y": -10.301},
    {"id": "E-5", "section_id": "E", "square_number": 5, "label": "E5", "is_active": True,  "x": -163.678, "y": -12.192},
    {"id": "E-6", "section_id": "E", "square_number": 6, "label": "E6", "is_active": True,  "x": -167.117, "y": -9.097},
    {"id": "E-7", "section_id": "E", "square_number": 7, "label": "E7", "is_active": True,  "x": -167.187, "y": -5.361},

    # Section F — Succulents and Xerophytes (6 squares)
    {"id": "F-1", "section_id": "F", "square_number": 1, "label": "F1", "is_active": True, "x": -152.603, "y": -5.250},
    {"id": "F-2", "section_id": "F", "square_number": 2, "label": "F2", "is_active": True, "x": -152.175, "y": -8.818},
    {"id": "F-3", "section_id": "F", "square_number": 3, "label": "F3", "is_active": True, "x": -155.697, "y": -12.192},
    {"id": "F-4", "section_id": "F", "square_number": 4, "label": "F4", "is_active": True, "x": -158.981, "y": -11.321},
    {"id": "F-5", "section_id": "F", "square_number": 5, "label": "F5", "is_active": True, "x": -158.101, "y": -6.006},
    {"id": "F-6", "section_id": "F", "square_number": 6, "label": "F6", "is_active": True, "x": -154.912, "y": -8.785},
]


async def seed():
    async with AsyncSessionLocal() as session:
        # Check if already seeded
        from sqlalchemy import select
        existing = await session.execute(select(Section).limit(1))
        if existing.scalar_one_or_none():
            print("Database already seeded. Skipping.")
            return

        print("Seeding sections...")
        for s in SECTIONS:
            session.add(Section(**s))

        print("Seeding squares...")
        for sq in SQUARES:
            session.add(Square(**sq))

        await session.commit()
        print(f"Done. {len(SECTIONS)} sections and {len(SQUARES)} squares seeded.")


if __name__ == "__main__":
    asyncio.run(seed())