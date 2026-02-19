# HematoVision Smartbridge

HematoVision Smartbridge is a blood-cell image classification project with two parts:

- A Next.js 16 frontend scaffold (UI components and layout).
- A Flask + TensorFlow web app that loads a pre-trained model to classify blood cell images.

The TensorFlow model file is stored at the repository root as Blood Cell.h5.

## Features

- Upload a blood-cell image and get a predicted label (eosinophil, lymphocyte, monocyte, neutrophil).
- Flask web UI with image preview and result screen.
- Next.js + Tailwind + shadcn/ui component library for building a modern frontend.

## Tech Stack

- Frontend: Next.js 16, React 19, Tailwind CSS, shadcn/ui, Radix UI
- Backend: Flask, TensorFlow, OpenCV, NumPy
- Model: Blood Cell.h5 (pre-trained)

## Project Structure

- app/ - Next.js app router layout and global styles
- components/ - Reusable UI components (shadcn/ui)
- Hematovision/ - Flask app, templates, and Python dependencies
- Blood Cell.h5 - TensorFlow model file required by the Flask app

## Frontend Setup (Next.js)

Use pnpm (recommended) or npm.

1. Install dependencies:

```bash
pnpm install
```

2. Start dev server:

```bash
pnpm dev
```

The app router currently contains only the layout in app/layout.tsx. Add pages under app/ (for example app/page.tsx) to build the UI.

## Backend Setup (Flask + TensorFlow)

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r Hematovision/requirements.txt
```

3. Run the Flask app:

```bash
cd Hematovision
python app.py
```

Open http://127.0.0.1:5000 and upload a JPG or PNG image.

## Model File Location (Important)

The Flask app looks for the model file in:

- The repository root: Blood Cell.h5
- Or next to Hematovision/app.py as a fallback

If you see a FileNotFoundError, place Blood Cell.h5 at the repository root or in the Hematovision folder.

## Scripts

- pnpm dev - Start Next.js development server
- pnpm build - Build Next.js
- pnpm start - Start Next.js production server
- pnpm lint - Run ESLint

## Notes

- Next.js config allows build with TypeScript errors (ignoreBuildErrors: true).
- Next.js image optimization is disabled (unoptimized: true).

## License

Add a license file if needed.
