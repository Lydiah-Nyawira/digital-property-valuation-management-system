# Digital Property Valuation Management System (DPVMS)

## Real Estate × Technology × Data

A PropTech platform designed to streamline property valuation workflows through digital property records management, comparable sales analysis, and data-driven reporting.

---

## Overview

The Digital Property Valuation Management System is a backend-focused application developed to support property valuation processes by providing a structured platform for managing property information, inspections, market evidence, and valuation records.

The system aims to bridge the gap between traditional real estate practices and modern software solutions.

---

## Problem Statement

Property valuation requires collecting, organizing, analyzing, and reporting large amounts of property information.

Traditional workflows may involve:
- Manual record keeping
- Disorganized property data
- Difficulty managing comparable evidence
- Time-consuming reporting processes

This project addresses these challenges by creating a centralized digital solution.

---

## Key Features

### Property Management
- Create and manage property records
- Store property details
- Maintain property information history
- Interactive location picker (map pin, search, or pasted map link)

### Inspection Management
- Record inspection details
- Store inspection notes
- Manage property images and documentation

### Comparable Sales Database
- Store comparable property information
- Organize market evidence
- Support comparative analysis

### Valuation Management
- Manage valuation records
- Store valuation methods
- Maintain valuation reports

### User Management
- Secure user authentication
- Role-based access control

---

## Technology Stack

### Backend
- Python
- Django
- Django REST Framework
- Pillow (image handling for inspection photos)

### Database
- PostgreSQL

### Mapping / GIS
- Leaflet.js
- OpenStreetMap
- Esri (satellite tiles)
- staticmap (Python library for generating report map images)

### Tools
- Git
- GitHub
- VS Code
- Postman

---

## System Architecture

```
Client
 |
REST API
 |
Django Backend
 |
PostgreSQL Database
 |
Property Data
```

---

## Installation

### Clone the repository

```bash
git clone repository-url
```

### Navigate into the project

```bash
cd digital-property-valuation-management-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python manage.py runserver
```

---

## API Documentation

API documentation will be provided as development progresses.

Main resources:

- Properties
- Users
- Inspections
- Comparable Sales
- Valuation Reports

---

## Database Design

The system is built around the following core entities and relationships:

- **User** — system users with role-based access (valuers, admins)
- **Client** — the party requesting a valuation
- **Property** — core property record (title number, location, county/sub-county, coordinates, land size, tenure, ownership type)
- **Valuation Assignment** — links a Property + Client to a specific valuation job; defines the valuation type (Full, Hybrid, Drive-By, Desktop)
- **Inspection Details** — site inspection data tied to an assignment; scope varies by valuation type
  - **Land Details**, **Building Details**, **Floor Details**, **Unit Details** — property hierarchy, linked through Inspection Details
  - **Inspection Photo** — categorized site images (access road, subject property, adjacent property, location maps, other)
- **Valuation Result** — the outcome of a valuation; holds market, mortgage, and insurance values plus reconciliation notes
  - **Cost Approach Detail**, **Income Approach Detail** — method-specific calculations linked to a Valuation Result
  - **Comparable Sale** — market approach comparables, one row per comparable property
- **External Market Evidence** — supporting market data used in valuations
- **Internal Valuation History** — completed valuations reused as comparables for future assignments
- **Assignment Comparable** — links comparable properties to a specific valuation assignment

**Relationship summary:** A Client requests a Valuation Assignment for a Property. Depending on the assignment's valuation type, an Inspection Details record (with its Land/Building/Floor/Unit hierarchy and photos) may or may not be created. Each assignment produces a Valuation Result, which can combine multiple valuation methods (Cost, Income, Market) reconciled into a final figure.

---

## Project Status

🚧 Currently under active development.

---

## Future Enhancements

Planned improvements include:

- Automated valuation support
- Market trend dashboards
- AI-assisted property analysis
- Digital property verification

---

## Screenshots

Screenshots and demonstrations will be added as features are completed.

---

## Contributing

Contributions, suggestions, and feedback are welcome.

---

## License

License information will be added.

---

## Author

**Lydiah Nyawira Mugweru**

Real Estate Management Graduate | Graduate Property Valuer | Backend Developer

Passionate about building solutions at the intersection of:

**Real Estate × Technology × Data**

### Connect

- GitHub: https://github.com/Lydiah-Nyawira
- LinkedIn: https://www.linkedin.com/in/lydiahnyawiram