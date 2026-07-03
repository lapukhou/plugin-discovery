# Discovery

A Claude Code plugin for product discovery. It structures raw app ideas and product concepts into **Use Case Maps** — a five-element framework (Problem, Persona, Alternative, Why, Frequency) that validates whether an opportunity is worth pursuing before anything gets built.

## Features

### `use-case-map` skill

Guides you through the Use Case Map framework:

- **Problem** — the specific issue users face, in their own words, scoped neither too broad nor too narrow
- **Persona** — who has the problem; splits distinct behaviors into separate use cases
- **Alternative** — how people cope today (not just direct competitors: Slack's alternative was email)
- **Why** — core motivation (Personal / Financial / Social) plus a concrete differentiator
- **Frequency** — how often the problem recurs, and whether the product lands in the Habit Zone or the Forgettable Zone

The skill is opportunity-first: give it a specific product idea and it extracts the underlying opportunities, then maps each one. It ends with a written `use-case-map.md` summary per opportunity and a stress test of the assumptions.

The skill activates automatically when you brainstorm app ideas, define a product concept, explore target customers, or think about product-market fit and retention. Just say something like:

> I have an app idea — an AI budget tracker for freelancers. Help me think it through.

## Installation

Add this repository as a marketplace, then install the plugin:

```
/plugin marketplace add lapukhou/plugin-discovery
/plugin install discovery@lapukhou-plugins
```

### Local development

To try the plugin from a local checkout:

```bash
claude --plugin-dir /path/to/plugin-discovery
```

## Structure

```
plugin-discovery/
├── .claude-plugin/
│   ├── plugin.json          # Plugin manifest
│   └── marketplace.json     # Marketplace listing (this repo doubles as a marketplace)
└── skills/
    └── use-case-map/
        ├── SKILL.md
        └── references/
            └── use-case-map-deep-dive.md   # Real-world examples (Figma, Thumbtack, HubSpot, ...)
```

## License

MIT
