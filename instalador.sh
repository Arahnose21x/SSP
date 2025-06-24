#!/data/data/com.termux/files/usr/bin/bash

echo "🔧 Instalando SSP (SimpleSpanishPython)..."

# Ruta al home
HOME_PATH=$HOME

# Clona si aún no está
if [ ! -d "$HOME_PATH/SSP" ]; then
    git clone https://github.com/TU_USUARIO/SSP.git $HOME_PATH/SSP
fi

# Crear alias en .bashrc
ALIAS_CMD='alias ssp="python3 ~/SSP/ssp_terminal.py"'
if ! grep -Fxq "$ALIAS_CMD" "$HOME_PATH/.bashrc"; then
    echo "$ALIAS_CMD" >> "$HOME_PATH/.bashrc"
    echo "✅ Alias 'ssp' añadido a .bashrc"
else
    echo "ℹ️ El alias ya está presente en .bashrc"
fi

# Crear alias en .zshrc si se usa zsh
if [ -f "$HOME_PATH/.zshrc" ]; then
    if ! grep -Fxq "$ALIAS_CMD" "$HOME_PATH/.zshrc"; then
        echo "$ALIAS_CMD" >> "$HOME_PATH/.zshrc"
        echo "✅ Alias 'ssp' añadido a .zshrc"
    fi
fi

# Recargar bashrc (solo para esta sesión)
source "$HOME_PATH/.bashrc"

echo "🎉 Instalación completada. Escribe 'ssp' para empezar."
