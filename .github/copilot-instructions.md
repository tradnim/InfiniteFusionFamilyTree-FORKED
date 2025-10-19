# InfiniteFusionCalculator (IFC) - AI Assistant Guide

## Project Overview
- Desktop calculator for Pokémon Infinite Fusion using PyQt6, showing evolution lines, stats and sprite fusions
- Core features: Single fusion calculator, Batch fusion processor, Type-based fusion search

## Architecture & Data Flow

### Core Components
- **Entry: `ifc/main.py`**
  - Bootstrap app via `QApplication` and `IFCWindow`
  - Handles Python path setup for absolute imports

- **Data Layer (`ifc/data/`)**
  - `pokedex.py`: Loads and indexes Pokémon data from CSV 
  - `pokemon.py`: Core classes for base/fused Pokémon with stat calculations
  - `utils.py`: Constants and fusion computation logic
  - `enums.py`: Type system with special `ANY` type handling

- **UI Layer (`ifc/gui/`)**
  - `window.py`: Main window setup, version checking
  - `tabs/*.py`: Mode implementations (Single/Batch/Type) using `IFCBaseTab`
  - `widgets.py`: Sprite display with URL-to-label mapping

- **Resources (`ifc/resources/`)**
  - `data.csv`: Source of truth for Pokémon stats/types
  - `fonts/pokemon_pixel_font.ttf`: Required UI font 
  - `images/`: Example images for documentation

### Key Data Flows
1. **Fusion Process**:
   ```
   UI Event -> get_fusions() -> FusedPokemon.__init__() 
   -> get_sprite_url() -> QNetworkAccessManager
   ```

2. **Sprite Loading Chain**:
   ```
   Base URL -> DigitalOcean CDN -> GitHub Custom Sprites 
   -> Fallback Paths -> Generated Sprites
   ```

## Developer Essentials

### Setup & Run
```powershell
# Development environment
python -m venv venv  # Python 3.8
.\venv\Scripts\activate
pip install -r requirements.txt

# Run app
python -m ifc.main   # Preferred way
# OR 
python main.py      # Alternative from project root

# Build distributable
python build_exe.py  # Creates dist/IFC.zip
```

### Critical Files for Changes
1. Adding/Modifying Fusions:
   - `pokemon.py`: `FusedPokemon.__init__()` for fusion rules
   - `utils.py`: `get_fusions()` for evolution handling
   
2. UI Customization:
   - `tabs/base.py`: Shared tab behaviors
   - `tabs/widgets.py`: Sprite handling and labels

3. Data Structure:
   - `data.csv`: Pokémon base data
   - `pokedex.py`: CSV loading and accessors

### Common Pitfalls
1. **Network Operations**
   - `IFCWindow` requires GitHub API access on startup
   - No built-in offline mode - version check asserts
   - Sprite URLs are case-sensitive
   
2. **Resource Loading**  
   - Font must exist at `resources/fonts/pokemon_pixel_font.ttf`
   - Font loading not cached despite frequent use
   - CSV schema changes need `pokedex.py` updates

3. **Type Safety**
   - Pokemon names in URLs need consistent casing
   - Type.ANY needs special equality handling
   - Evolution line IDs must match CSV index

## Testing & Validation 

### Test Approach
The project has no formal tests. Verify changes by:

1. Manual Testing:
   ```python
   from ifc.data import pokedex, pokemon
   poke = pokedex.get_pokemon(name="Charizard")
   assert len(poke.types) > 0
   ```

2. Visual Checks:
   - Run app, test all 3 modes
   - Verify sprite loading chains
   - Check fusion stat calculations

### Key Test Cases
1. Evolution Line Merging:
   ```python
   head = "Charmander"  # 3-stage evolution
   body = "Squirtle"    # 3-stage evolution
   fusions = utils.get_fusions(head, body)
   assert len(fusions[0]) == 9  # All combinations
   ```

2. Type Inheritance:
   ```python
   fusion = FusedPokemon(fire_poke, water_poke)
   assert fusion.types[0] == fire_poke.types[0]
   assert fusion.types[1] in water_poke.types
   ```

## Best Practices for AI Assistance

### Code Changes
- Reference specific functions/paths in suggestions
- Provide test snippets with imports and assertions  
- Don't modify sprite URL fallback chain without discussion

### Review Focus
1. UI Layer:
   - Check font usage frequency
   - Verify sprite loading error handling
   - Maintain tab behavior consistency

2. Data Layer:  
   - Validate CSV column usage
   - Check type system edge cases
   - Verify evolution line integrity

### Key Questions to Ask
- Network resilience requirements?
- Preferred sprite normalization approach?
- Performance requirements for repeated operations?