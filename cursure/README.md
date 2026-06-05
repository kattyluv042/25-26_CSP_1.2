# Python Drawing App

A simple pygame drawing canvas with a custom color palette, eraser, and brush sizes 1–35.

## Open in PyCharm

1. **File → Open** and choose this folder: `C:\Users\23111\python-drawing-app`
2. Run the setup script once (creates `.venv` and installs pygame):

   ```powershell
   .\setup.ps1
   ```

3. In PyCharm: **File → Settings → Project → Python Interpreter**
   - Click the gear → **Add Interpreter → Add Local Interpreter**
   - Choose **Existing** and select `.venv\Scripts\python.exe` in this project
4. Use the pre-made run config: select **Drawing App** in the top toolbar and click the green **Run** button.

You can also right-click `drawing_app.py` → **Run 'drawing_app'**.

## Setup (terminal, without PyCharm)

```powershell
.\setup.ps1
.\.venv\Scripts\python.exe drawing_app.py
```

Or install globally:

```bash
pip install -r requirements.txt
python drawing_app.py
```

## Controls

- **Click + drag** on the canvas to draw
- **Space** — cycle through colors in the palette list
- **1** — increase brush size (1 through 35, then wraps back to 1)
- **Eraser** button (bottom left) — switch to white eraser mode

Instructions also appear in the top-right corner while the app runs.
