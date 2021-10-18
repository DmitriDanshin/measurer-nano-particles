module.exports = {
    root: true,
    env: {
        node: true
    },
    'extends': [
        'plugin:vue/vue3-essential',
        'eslint:recommended'
    ],
    parserOptions: {
        parser: 'babel-eslint'
    },
    rules: {
        'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        'no-debugger': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
        "vue/max-attributes-per-line": [
            "warn",
            {
                "singleline": {
                    "max": 1,
                    "allowFirstLine": true
                },
                "multiline": {
                    "max": 1,
                    "allowFirstLine": false
                }
            }
        ],
        "vue/html-closing-bracket-newline": [
            "error",
            {
                "singleline": "never",
                "multiline": "always"
            }
        ],
        "vue/attributes-order": [
            "error",
            {
                "order": [
                    "DEFINITION",
                    "LIST_RENDERING",
                    "CONDITIONALS",
                    "RENDER_MODIFIERS",
                    "GLOBAL",
                    [
                        "UNIQUE",
                        "SLOT"
                    ],
                    "TWO_WAY_BINDING",
                    "OTHER_DIRECTIVES",
                    "OTHER_ATTR",
                    "EVENTS",
                    "CONTENT"
                ],
                "alphabetical": false
            }
        ],
        "prettier/prettier": "off"
    }
}

