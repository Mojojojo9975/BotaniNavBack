from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import uvicorn

app = FastAPI(
    title="Botanical Garden Mock API",
    version="1.0.0",
    description="Mock API for frontend MVP development"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Real sections from DXF ─────────────────────────────────────────────────────

SECTIONS = {
    "A": {
        "id": "A",
        "name": "Tropical Section",
        "finnishName": "Trooppinen osasto",
        "greenhouse_id": 1,
        "center_x": -137.345,
        "center_y": 13.048,
        "entry_x": -142.000,
        "entry_y": 12.226
    },
    "B": {
        "id": "B",
        "name": "Sub Tropical Section",
        "finnishName": "Subtrooppisten kesäsateiden osasto",
        "greenhouse_id": 1,
        "center_x": -128.153,
        "center_y": 8.881,
        "entry_x": -130.650,
        "entry_y": 10.612
    },
    "D": {
        "id": "D",
        "name": "Mediterranean Section",
        "finnishName": "Subtrooppisten talvisateiden osasto",
        "greenhouse_id": 2,
        "center_x": -158.208,
        "center_y": -1.851,
        "entry_x": -154.360,
        "entry_y": 2.805
    },
    "E": {
        "id": "E",
        "name": "Temperate Climate Section",
        "finnishName": "Lauhkean ilmaston osasto",
        "greenhouse_id": 2,
        "center_x": -163.483,
        "center_y": -7.163,
        "entry_x": -161.400,
        "entry_y": -5.985
    },
    "F": {
        "id": "F",
        "name": "Succulents and Xerophytes",
        "finnishName": "Sukkulentti- ja kserofyyttiosasto",
        "greenhouse_id": 2,
        "center_x": -155.997,
        "center_y": -8.168,
        "entry_x": -152.603,
        "entry_y": -5.250
    }
}

SQUARES = {
    # Section A
    "A-1":  {"id": "A-1",  "section_id": "A", "label": "A1",  "is_active": True,  "x": -142.000, "y": 12.226},
    "A-2":  {"id": "A-2",  "section_id": "A", "label": "A2",  "is_active": True,  "x": -139.549, "y": 16.513},
    "A-3":  {"id": "A-3",  "section_id": "A", "label": "A3",  "is_active": True,  "x": -133.239, "y": 21.837},
    "A-3B": {"id": "A-3B", "section_id": "A", "label": "A3",  "is_active": True,  "x": -127.743, "y": 21.872},
    "A-4":  {"id": "A-4",  "section_id": "A", "label": "A4",  "is_active": True,  "x": -124.180, "y": 18.376},
    "A-5":  {"id": "A-5",  "section_id": "A", "label": "A5",  "is_active": True,  "x": -125.560, "y": 14.620},
    "A-6":  {"id": "A-6",  "section_id": "A", "label": "A6",  "is_active": True,  "x": -129.510, "y": 14.172},
    "A-7":  {"id": "A-7",  "section_id": "A", "label": "A7",  "is_active": True,  "x": -128.298, "y": 18.380},
    "A-8":  {"id": "A-8",  "section_id": "A", "label": "A8",  "is_active": True,  "x": -134.000, "y": 19.026},
    "A-9":  {"id": "A-9",  "section_id": "A", "label": "A9",  "is_active": True,  "x": -133.090, "y": 16.733},
    "A-10": {"id": "A-10", "section_id": "A", "label": "A10", "is_active": True,  "x": -135.518, "y": 15.476},
    "A-11": {"id": "A-11", "section_id": "A", "label": "A11", "is_active": True,  "x": -134.268, "y": 13.991},
    "A-12": {"id": "A-12", "section_id": "A", "label": "A12", "is_active": True,  "x": -138.679, "y": 11.764},
    "A-13": {"id": "A-13", "section_id": "A", "label": "A13", "is_active": True,  "x": -138.818, "y": 8.726},
    "A-14": {"id": "A-14", "section_id": "A", "label": "A14", "is_active": True,  "x": -134.418, "y": 9.926},
    "A-15": {"id": "A-15", "section_id": "A", "label": "A15", "is_active": True,  "x": -134.868, "y": 5.826},
    "A-16": {"id": "A-16", "section_id": "A", "label": "A16", "is_active": True,  "x": -138.087, "y": 4.426},
    "A-17": {"id": "A-17", "section_id": "A", "label": "A17", "is_active": True,  "x": -141.942, "y": 5.999},
    # Section B
    "B-1": {"id": "B-1", "section_id": "B", "label": "B1", "is_active": True, "x": -130.650, "y": 10.612},
    "B-2": {"id": "B-2", "section_id": "B", "label": "B2", "is_active": True, "x": -125.200, "y": 11.726},
    "B-3": {"id": "B-3", "section_id": "B", "label": "B3", "is_active": True, "x": -124.173, "y": 7.826},
    "B-4": {"id": "B-4", "section_id": "B", "label": "B4", "is_active": True, "x": -127.625, "y": 4.426},
    "B-5": {"id": "B-5", "section_id": "B", "label": "B5", "is_active": True, "x": -131.350, "y": 5.576},
    "B-6": {"id": "B-6", "section_id": "B", "label": "B6", "is_active": True, "x": -127.885, "y": 7.376},
    # Section D
    "D-1":  {"id": "D-1",  "section_id": "D", "label": "D1",  "is_active": True, "x": -154.360, "y": 2.805},
    "D-2":  {"id": "D-2",  "section_id": "D", "label": "D2",  "is_active": True, "x": -152.098, "y": -0.545},
    "D-3":  {"id": "D-3",  "section_id": "D", "label": "D3",  "is_active": True, "x": -153.960, "y": -4.151},
    "D-4":  {"id": "D-4",  "section_id": "D", "label": "D4",  "is_active": True, "x": -158.020, "y": -3.425},
    "D-5":  {"id": "D-5",  "section_id": "D", "label": "D5",  "is_active": True, "x": -155.891, "y": -0.433},
    "D-6":  {"id": "D-6",  "section_id": "D", "label": "D6",  "is_active": True, "x": -161.724, "y": -3.971},
    "D-7":  {"id": "D-7",  "section_id": "D", "label": "D7",  "is_active": True, "x": -167.197, "y": -4.135},
    "D-8":  {"id": "D-8",  "section_id": "D", "label": "D8",  "is_active": True, "x": -162.824, "y": -0.273},
    "D-9":  {"id": "D-9",  "section_id": "D", "label": "D9",  "is_active": True, "x": -161.770, "y": -0.385},
    "D-10": {"id": "D-10", "section_id": "D", "label": "D10", "is_active": True, "x": -165.393, "y": 2.688},
    # Section E
    "E-1": {"id": "E-1", "section_id": "E", "label": "E1", "is_active": True,  "x": -161.400, "y": -5.985},
    "E-2": {"id": "E-2", "section_id": "E", "label": "E2", "is_active": True,  "x": -163.939, "y": -8.535},
    "E-3": {"id": "E-3", "section_id": "E", "label": "E3", "is_active": False, "x": -164.403, "y": -8.103},
    "E-4": {"id": "E-4", "section_id": "E", "label": "E4", "is_active": True,  "x": -160.164, "y": -10.301},
    "E-5": {"id": "E-5", "section_id": "E", "label": "E5", "is_active": True,  "x": -163.678, "y": -12.192},
    "E-6": {"id": "E-6", "section_id": "E", "label": "E6", "is_active": True,  "x": -167.117, "y": -9.097},
    "E-7": {"id": "E-7", "section_id": "E", "label": "E7", "is_active": True,  "x": -167.187, "y": -5.361},
    # Section F
    "F-1": {"id": "F-1", "section_id": "F", "label": "F1", "is_active": True, "x": -152.603, "y": -5.250},
    "F-2": {"id": "F-2", "section_id": "F", "label": "F2", "is_active": True, "x": -152.175, "y": -8.818},
    "F-3": {"id": "F-3", "section_id": "F", "label": "F3", "is_active": True, "x": -155.697, "y": -12.192},
    "F-4": {"id": "F-4", "section_id": "F", "label": "F4", "is_active": True, "x": -158.981, "y": -11.321},
    "F-5": {"id": "F-5", "section_id": "F", "label": "F5", "is_active": True, "x": -158.101, "y": -6.006},
    "F-6": {"id": "F-6", "section_id": "F", "label": "F6", "is_active": True, "x": -154.912, "y": -8.785},
}

# ── Mock plants using real sections and squares ────────────────────────────────

PLANTS = [
    {
        "taxonNumber": 1001,
        "name": "Monstera deliciosa",
        "synonym": "Philodendron pertusum",
        "finnishName": "Sveitsinjuustokasvi",
        "family": {"name": "Araceae"},
        "placement": {
            "placementLocationNumber": 2001,
            "placementDate": "2022-03-15",
            "square": "A-12",
            "placementLocationName": "Tropical Section",
            "plantStatus": "Healthy",
            "plantComments": "Large mature specimen",
            "departmentNumber": 1
        }
    },
    {
        "taxonNumber": 1002,
        "name": "Victoria amazonica",
        "synonym": "Victoria regia",
        "finnishName": "Jättiläisvesililja",
        "family": {"name": "Nymphaeaceae"},
        "placement": {
            "placementLocationNumber": 2002,
            "placementDate": "2021-06-01",
            "square": "A-8",
            "placementLocationName": "Tropical Section",
            "plantStatus": "Healthy",
            "plantComments": "Requires large water feature",
            "departmentNumber": 1
        }
    },
    {
        "taxonNumber": 1003,
        "name": "Strelitzia reginae",
        "synonym": "Strelitzia parvifolia",
        "finnishName": "Paratiisilintukasvit",
        "family": {"name": "Strelitziaceae"},
        "placement": {
            "placementLocationNumber": 2003,
            "placementDate": "2020-11-20",
            "square": "B-3",
            "placementLocationName": "Sub Tropical Section",
            "plantStatus": "Healthy",
            "plantComments": "Near south wall",
            "departmentNumber": 1
        }
    },
    {
        "taxonNumber": 1004,
        "name": "Ficus benjamina",
        "synonym": "Ficus nitida",
        "finnishName": "Koivuviikunapuu",
        "family": {"name": "Moraceae"},
        "placement": {
            "placementLocationNumber": 2004,
            "placementDate": "2019-08-10",
            "square": "B-6",
            "placementLocationName": "Sub Tropical Section",
            "plantStatus": "Needs attention",
            "plantComments": "Minor leaf discolouration observed",
            "departmentNumber": 1
        }
    },
    {
        "taxonNumber": 1005,
        "name": "Olea europaea",
        "synonym": "Olea europaea var. sativa",
        "finnishName": "Euroopanöljypuu",
        "family": {"name": "Oleaceae"},
        "placement": {
            "placementLocationNumber": 2005,
            "placementDate": "2018-04-22",
            "square": "D-5",
            "placementLocationName": "Mediterranean Section",
            "plantStatus": "Healthy",
            "plantComments": "Mature specimen",
            "departmentNumber": 2
        }
    },
    {
        "taxonNumber": 1006,
        "name": "Nerium oleander",
        "synonym": "Nerium indicum",
        "finnishName": "Oleanteri",
        "family": {"name": "Apocynaceae"},
        "placement": {
            "placementLocationNumber": 2006,
            "placementDate": "2017-09-05",
            "square": "D-9",
            "placementLocationName": "Mediterranean Section",
            "plantStatus": "Healthy",
            "plantComments": "Pink flowering variety",
            "departmentNumber": 2
        }
    },
    {
        "taxonNumber": 1007,
        "name": "Quercus robur",
        "synonym": "Quercus pedunculata",
        "finnishName": "Tammi",
        "family": {"name": "Fagaceae"},
        "placement": {
            "placementLocationNumber": 2007,
            "placementDate": "2016-03-10",
            "square": "E-4",
            "placementLocationName": "Temperate Climate Section",
            "plantStatus": "Healthy",
            "plantComments": "Native Finnish species",
            "departmentNumber": 2
        }
    },
    {
        "taxonNumber": 1008,
        "name": "Betula pendula",
        "synonym": "Betula alba",
        "finnishName": "Rauduskoivu",
        "family": {"name": "Betulaceae"},
        "placement": {
            "placementLocationNumber": 2008,
            "placementDate": "2015-05-01",
            "square": "E-7",
            "placementLocationName": "Temperate Climate Section",
            "plantStatus": "Healthy",
            "plantComments": "Along northern boundary",
            "departmentNumber": 2
        }
    },
    {
        "taxonNumber": 1009,
        "name": "Aloe vera",
        "synonym": "Aloe barbadensis",
        "finnishName": "Lääkealoe",
        "family": {"name": "Asphodelaceae"},
        "placement": {
            "placementLocationNumber": 2009,
            "placementDate": "2021-02-14",
            "square": "F-2",
            "placementLocationName": "Succulents and Xerophytes",
            "plantStatus": "Healthy",
            "plantComments": "Large colony",
            "departmentNumber": 2
        }
    },
    {
        "taxonNumber": 1010,
        "name": "Euphorbia canariensis",
        "synonym": "Euphorbia canariensis var. typica",
        "finnishName": "Kanarianeuphorbia",
        "family": {"name": "Euphorbiaceae"},
        "placement": {
            "placementLocationNumber": 2010,
            "placementDate": "2020-07-20",
            "square": "F-5",
            "placementLocationName": "Succulents and Xerophytes",
            "plantStatus": "Healthy",
            "plantComments": "Candelabra form",
            "departmentNumber": 2
        }
    },
    {
        "taxonNumber": 1011,
        "name": "Nepenthes rajah",
        "synonym": "Nepenthes rajah var. typica",
        "finnishName": "Kannukasvi",
        "family": {"name": "Nepenthaceae"},
        "placement": {
            "placementLocationNumber": 2011,
            "placementDate": "2023-01-10",
            "square": "A-3",
            "placementLocationName": "Tropical Section",
            "plantStatus": "Healthy",
            "plantComments": "Humidity controlled zone",
            "departmentNumber": 1
        }
    },
    {
        "taxonNumber": 1012,
        "name": "Cycas revoluta",
        "synonym": "Cycas miquelii",
        "finnishName": "Käpypalmu",
        "family": {"name": "Cycadaceae"},
        "placement": {
            "placementLocationNumber": 2012,
            "placementDate": "2016-07-30",
            "square": "D-2",
            "placementLocationName": "Mediterranean Section",
            "plantStatus": "Healthy",
            "plantComments": "Oldest specimen in collection",
            "departmentNumber": 2
        }
    },
]

# ── Enrichment helper ──────────────────────────────────────────────────────────

def enrich_plant(plant: dict) -> dict:
    square_id = plant["placement"]["square"]
    square = SQUARES.get(square_id)
    section = SECTIONS.get(square["section_id"]) if square else None

    return {
        **plant,
        "enriched": {
            "square_id": square_id,
            "square_x": square["x"] if square else None,
            "square_y": square["y"] if square else None,
            "section_id": section["id"] if section else None,
            "section_name": section["name"] if section else None,
            "section_finnish_name": section["finnishName"] if section else None,
            "greenhouse_id": section["greenhouse_id"] if section else None,
            "section_center_x": section["center_x"] if section else None,
            "section_center_y": section["center_y"] if section else None,
            "section_entry_x": section["entry_x"] if section else None,
            "section_entry_y": section["entry_y"] if section else None,
        }
    }

# ── Endpoints ──────────────────────────────────────────────────────────────────

@app.get("/api/v1/plants")
async def get_plants(
    section: Optional[str] = Query(None, description="Filter by section id e.g. A, B, D, E, F"),
    status: Optional[str] = Query(None, description="Filter by plantStatus"),
    greenhouse: Optional[int] = Query(None, description="Filter by greenhouse_id 1 or 2"),
    search: Optional[str] = Query(None, description="Search by name or finnish name")
):
    results = [enrich_plant(p) for p in PLANTS]

    if section:
        results = [
            r for r in results
            if r["enriched"]["section_id"] == section.upper()
        ]
    if status:
        results = [
            r for r in results
            if r["placement"]["plantStatus"].lower() == status.lower()
        ]
    if greenhouse:
        results = [
            r for r in results
            if r["enriched"]["greenhouse_id"] == greenhouse
        ]
    if search:
        term = search.lower()
        results = [
            r for r in results
            if term in r["name"].lower() or term in r["finnishName"].lower()
        ]

    return {
        "count": len(results),
        "plants": results
    }


@app.get("/api/v1/plants/{taxon_number}")
async def get_plant(taxon_number: int):
    plant = next(
        (p for p in PLANTS if p["taxonNumber"] == taxon_number),
        None
    )
    if not plant:
        raise HTTPException(status_code=404, detail="Plant not found")
    return enrich_plant(plant)


@app.get("/api/v1/sections")
async def get_sections():
    result = []
    for section in SECTIONS.values():
        plant_count = sum(
            1 for p in PLANTS
            if SQUARES.get(p["placement"]["square"], {}).get("section_id") == section["id"]
        )
        squares = [
            sq for sq in SQUARES.values()
            if sq["section_id"] == section["id"] and sq["is_active"]
        ]
        result.append({
            **section,
            "plant_count": plant_count,
            "active_squares": len(squares),
            "squares": squares
        })
    return {"count": len(result), "sections": result}


@app.get("/api/v1/sections/{section_id}")
async def get_section(section_id: str):
    section = SECTIONS.get(section_id.upper())
    if not section:
        raise HTTPException(status_code=404, detail="Section not found")

    squares = [
        sq for sq in SQUARES.values()
        if sq["section_id"] == section_id.upper()
    ]
    plants = [
        enrich_plant(p) for p in PLANTS
        if SQUARES.get(p["placement"]["square"], {}).get("section_id") == section_id.upper()
    ]
    return {
        **section,
        "squares": squares,
        "plants": plants,
        "plant_count": len(plants)
    }


@app.get("/api/v1/squares/{square_id}")
async def get_square(square_id: str):
    square = SQUARES.get(square_id.upper())
    if not square:
        raise HTTPException(status_code=404, detail="Square not found")
    section = SECTIONS.get(square["section_id"])
    plants = [
        enrich_plant(p) for p in PLANTS
        if p["placement"]["square"] == square_id.upper()
    ]
    return {
        **square,
        "section": section,
        "plants": plants
    }


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "mode": "mock",
        "total_plants": len(PLANTS),
        "total_sections": len(SECTIONS),
        "total_squares": len(SQUARES)
    }


if __name__ == "__main__":
    uvicorn.run("mock_api:app", host="0.0.0.0", port=8001, reload=True)