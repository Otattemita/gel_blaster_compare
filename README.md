# Tactical Arsenal Intelligence

![Deploy static content to Pages](https://github.com/Otattemita/gel_blaster_compare/actions/workflows/deploy.yml/badge.svg)

This project is a high-fidelity technical wiki for the Gel Blaster community, featuring cross-referenced intelligence from Chinese technical forums and real-time stock data.

## Deployment

This project is configured for automated deployment to GitHub Pages via GitHub Actions.

### Setup Instructions

1.  **Enable GitHub Pages**:
    -   Go to your repository on GitHub.
    -   Navigate to **Settings** > **Pages**.
    -   Under **Build and deployment** > **Source**, select **GitHub Actions**.
2.  **Push Changes**:
    -   Any push to the `main` branch will automatically trigger the `Deploy static content to Pages` workflow.
    -   The site will be available at: `https://Otattemita.github.io/gel_blaster_compare/`

## Development

```bash
npm install
npm run dev
```

## Technology Stack

- **Frontend**: React + Vite
- **Animations**: Framer Motion
- **Icons**: Lucide React
- **Data Intelligence**: Automated Python backend tools (see `backend_tools/`)
