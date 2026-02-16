# Limoka - Module Library for Hikka

## Description

Limoka is an open-source repository hosting modules for Hikka, a modular Telegram userbot built on the Telethon library. The core module, `Limoka.py`, provides advanced search functionality within Telegram, while additional community-contributed modules extend Hikka with various tools and features. Developers can submit new modules via a [Telegram bot](https://t.me/limoka_applicationbot) for review and inclusion in the repository.

Limoka serves as a centralized library, enabling users to enhance their Telegram experience through Python-based automation scripts integrated with Hikka.

## Technology Stack

- **Python**: Core language for module development, leveraging Python's simplicity and extensive ecosystem.
- **Aiohttp**: For some requests to limoka repository
- **Whoosh**: Search engine
- **Hikka**: The userbot framework that Limoka modules extend, built on Telethon for Telegram API interactions.
- **Git**: Version control for managing the repository and community contributions.
- **CI/CD Tools**: Automated pipelines for testing and deploying module updates (see Infrastructure section).
- **Optional Dependencies**: Libraries like `requests`, `aiohttp`, or `beautifulsoup4` for parsing or external API interactions, depending on module requirements.
- **Parsing Tools**: Custom scripts using `ast` and `json` for extracting module metadata and commands.

## Usage

Once installed, Limoka modules are accessible via Hikka's command system in any Telegram chat where the userbot is active. The primary `Limoka.py` module enables search functionality with commands like `.limoka [query]`. Other modules may provide additional utilities, such as media processing or automation.

To explore available commands:

- Use `.help` to list all loaded modules.
- Use `.help [module_name]` for specific module documentation.

Refer to module docstrings or embedded documentation for detailed command usage.

## Installation

To integrate the Limoka module into your Hikka setup, follow these steps:

1. **Ensure Hikka is Installed**:

   - Install Hikka by following the official guide: Hikka Installation.
   - Verify that Hikka is running and accessible via Telegram.

2. **Install the Core Limoka Module**:

   - In a Telegram chat where Hikka is active, run:

     ```bash
     .dlm https://raw.githubusercontent.com/MuRuLOSE/limoka/refs/heads/main/Limoka.py
     ```
   - This command downloads and installs the `Limoka.py` module directly into Hikka.

3. **Verify Installation**:

   - Use `.help` to confirm that the Limoka module is loaded.
   - Check module-specific commands with `.help Limoka`.

4. **Optional: Install Additional Modules**:

   - Use `.dlm` with the module URL.

## Infrastructure

Limoka's infrastructure supports module development, contribution, and maintenance. Key components include:

- **Modules**:
  - **Search**: The core `Limoka.py` module for advanced search functionality in Telegram.
  - **Other Tools**: Community-contributed modules for tasks like media processing, automation, or notifications.
- **Repository**:
  - Hosted on GitHub, enabling version control and pull request-based contributions.
- **Parsing**:
  - Custom Python scripts using `ast` and `json` to parse module metadata (e.g., developer info, commands, and docstrings) and generate `modules.json` and `developers.json` files.
  - Supports extraction of `ru_doc`, `en_doc`, and other metadata for documentation purposes.
- **Backups**:
  - Regular backups of the repository to ensure data integrity and recovery.
- **AI Categories**:
  - AI-driven features, such as module categorization, depending on module implementations.
- **CI/CD**:
  - Automated pipelines for testing module compatibility with Hikka and deploying updates to the repository.
- **Moderation**:
  - All modules undergo moderation by Limoka reviewers.

## Contributing

Limoka is a community-driven project, and contributions are welcome through two primary methods:

1. **Applying to Become a Developer**:

   - Contact the Limoka team via the Telegram bot: t.me/limoka_applicationbot.
   - Submit details about your proposed module, including its functionality, purpose, and any relevant technical details.
   - Upon approval, you will receive instructions to proceed with development and submission.

2. **Contributing Code via Fork**:

   - Fork the repository: github.com/MuRuLOSE/limoka.
   - Make your changes
   - Submit a pull request with a clear description of your changes.
   - Maintainers will review your pull request for functionality, compatibility, and code quality.

   ### DONT PULL REQUEST YOUR MODULES!

## License

This project is licensed under the MIT License.

## Contact

For questions, feedback, or module submission inquiries, contact the Limoka team:

- Telegram (Feedback): t.me/limoka_feedback_bot
- Telegram (Module Applications): t.me/limoka_applicationbot
- GitHub Issues: github.com/MuRuLOSE/limoka/issues