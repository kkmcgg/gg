# main.py
import logging
import datetime
from pathlib import Path # Use pathlib for easier path handling

log = logging.getLogger("mkdocs.plugins.macros")

# --- Configuration for Discovery ---
# Directory containing files to scan for headers (relative to your docs_dir)
SCAN_DIR_FOR_HEADERS = "glossary"
# ---

# Store discovered headers (using a global is simple for this example, could also attach to env)
discovered_headers = {}

def define_env(env): # just does the scanning
    """
    This hook runs once. We will:
    1. Discover headers using simple file reading.
    2. Store the results in env.variables.
    3. Define the test macro from before.
    """
    log.info("DISCOVERY+MACRO TEST: define_env hook running.")

    # Reset map for 'mkdocs serve' auto-reloads
    global discovered_headers
    discovered_headers = {}

    # --- 1. Header Discovery Logic (Simplified) ---
    # Get the absolute path to the docs directory from MkDocs config
    docs_dir = Path(env.conf['docs_dir'])
    # Calculate the absolute path to the directory to scan
    scan_path = docs_dir / SCAN_DIR_FOR_HEADERS

    # Check if the scan directory exists
    if not scan_path.is_dir():
        log.warning(f"DISCOVERY+MACRO TEST: Scan directory '{scan_path}' not found. Cannot discover headers.")
    else:
        log.info(f"DISCOVERY+MACRO TEST: Scanning for headers in '{scan_path}'...")
        # Iterate through items in the scan directory
        for item in scan_path.iterdir():
            # Process only markdown files
            if item.is_file() and item.suffix == ".md":
                try:
                    # Open and read the file
                    with open(item, 'r', encoding='utf-8') as f:
                        for line in f:
                            stripped_line = line.strip()
                            # Find the first line starting with '# '
                            if stripped_line.startswith("# "):
                                header_text = stripped_line[2:].strip() # Text after '# '
                                if header_text: # Ensure it's not empty
                                    filename_stem = item.stem # Filename without .md
                                    # Store mapping (first found wins if duplicates)
                                    if header_text not in discovered_headers:
                                        discovered_headers[header_text] = filename_stem
                                        log.info(f"  Discovered: '{header_text}' in '{filename_stem}.md'")
                                    # else: you could add a warning here if needed
                                    break # Stop reading this file after finding the first H1
                except Exception as e:
                    log.error(f"  Error reading file {item.name}: {e}")
        log.info(f"DISCOVERY+MACRO TEST: Discovery finished. Found {len(discovered_headers)} headers.")

    # --- Store results for use in Markdown ---
    # Make the discovered map available as {{ discovered_header_map }}
    env.variables['discovered_header_map'] = discovered_headers
    # Also make the config path available for display
    env.variables['SCAN_DIR_FOR_HEADERS_CONFIG'] = SCAN_DIR_FOR_HEADERS

    # --- 2. Simple Test Macro (from previous working test) ---
    @env.macro
    def basic_test_macro():
        """A simple macro that logs a message when called."""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        message = f"MACRO TEST: basic_test_macro() executed at {timestamp}!"
        log.info(message)
        # Return the message so it appears on the page too
        return message

    log.info("DISCOVERY+MACRO TEST: Registered basic_test_macro.")
    log.info("DISCOVERY+MACRO TEST: define_env finished.")

    # We *still* haven't registered env.page_markdown_hook for auto-linking yet.
    # This script just does discovery and provides the test macro.


##################### version 2, attempts to actually implemet uto linking
# # main.py
# import os
# import re
# import logging
# import datetime
# from pathlib import Path

# # --- Slugify Function (Attempt import, provide fallback) ---
# # We need this to create the #anchor-link part
# log_slug = logging.getLogger("mkdocs.plugins.macros.slugify")
# try:
#     from markdown.extensions.toc import slugify as official_slugify
#     slugify_func = official_slugify
#     log_slug.info("Using slugify function from markdown.extensions.toc (if available).")
# except ImportError:
#     log_slug.warning("Could not import slugify from markdown.extensions.toc. Using simple fallback slugify.")
#     def simple_slugify(text):
#         # Simple slugify: lowercase, remove non-alphanumeric/space/hyphen, replace space/multiple hyphens with single hyphen
#         text = re.sub(r'[^\w\s-]', '', text.strip().lower())
#         return re.sub(r'[-\s]+', '-', text)
#     slugify_func = simple_slugify
# # ---

# log = logging.getLogger("mkdocs.plugins.macros")

# # --- Configuration ---
# # Directory containing files to scan for headers (relative to your docs_dir)
# SCAN_DIR_FOR_HEADERS = "glossary"
# # Link only the first occurrence of each header text on a given page?
# LINK_FIRST_OCCURRENCE_ONLY = True
# # Match header text case-sensitively when linking? (False is usually better)
# CASE_SENSITIVE = False
# # --- End Configuration ---

# # Store discovered data globally for access by helper function
# # Format: {header_key: (filename_stem, slug, original_header_text)}
# discovered_link_data = {}
# # Compiled regex patterns (prepared once for efficiency)
# term_pattern_for_linking = None
# exclude_pattern_for_linking = None

# def define_env(env):
#     """
#     This hook runs once. It will:
#     1. Discover headers AND slugs using simple file reading.
#     2. Prepare regex patterns.
#     3. Define and register the markdown hook for auto-linking.
#     """
#     log.info("AUTO-LINKING: define_env hook running.")
#     global discovered_link_data, term_pattern_for_linking, exclude_pattern_for_linking

#     # --- 1. Header Discovery (Simplified, now includes slug) ---
#     discovered_link_data = {} # Reset for serve mode rebuilds
#     docs_dir = Path(env.conf['docs_dir'])
#     scan_path = docs_dir / SCAN_DIR_FOR_HEADERS

#     if not scan_path.is_dir():
#         log.warning(f"AUTO-LINKING: Scan directory '{scan_path}' not found. Cannot discover headers.")
#     else:
#         log.info(f"AUTO-LINKING: Scanning for headers in '{scan_path}'...")
#         for item in scan_path.iterdir():
#             if item.is_file() and item.suffix == ".md":
#                 try:
#                     with open(item, 'r', encoding='utf-8') as f:
#                         for line in f:
#                             stripped_line = line.strip()
#                             if stripped_line.startswith("# "): # Find first H1
#                                 header_text = stripped_line[2:].strip()
#                                 if header_text:
#                                     filename_stem = item.stem
#                                     # Generate the URL slug for the anchor link
#                                     slug = slugify_func(header_text)
#                                     # Determine dictionary key based on case sensitivity
#                                     header_key = header_text if CASE_SENSITIVE else header_text.lower()

#                                     # Store if not already found (first wins)
#                                     if header_key not in discovered_link_data:
#                                         discovered_link_data[header_key] = (filename_stem, slug, header_text)
#                                         log.info(f"  Discovered: '{header_text}' -> {filename_stem}.md#{slug}")
#                                     break # Stop reading this file after finding the first H1
#                 except Exception as e:
#                     log.error(f"  Error reading file {item.name}: {e}")
#         log.info(f"AUTO-LINKING: Discovery finished. Found {len(discovered_link_data)} unique headers for linking.")

#     # Store for optional display on page (can be removed if not needed)
#     env.variables['discovered_header_map_for_linking'] = discovered_link_data

#     # --- 2. Prepare Regex Patterns (only if terms were found) ---
#     if discovered_link_data:
#         header_keys = list(discovered_link_data.keys())
#         # Escape keys for regex safety, sort longest first for correct matching
#         escaped_keys = sorted([re.escape(key) for key in header_keys], key=len, reverse=True)
#         # Build pattern \b(Key1|Key2|...)\b for whole-word matching
#         pattern_str = r'\b(' + '|'.join(escaped_keys) + r')\b'
#         # Compile regex for efficiency
#         term_pattern_for_linking = re.compile(pattern_str, 0 if CASE_SENSITIVE else re.IGNORECASE)

#         # Compile exclude pattern (same as before)
#         exclude_pattern_for_linking = re.compile(
#             r'(`{1,3}.*?`{1,3})|'          # Code spans or blocks
#             r'(\[.*?\]\(.*?\))|'         # Markdown links
#             r'(<.*?>)',                   # HTML tags
#             re.DOTALL | re.MULTILINE
#         )
#         log.info(f"AUTO-LINKING: Prepared regex for {len(discovered_link_data)} terms.")
#     else:
#          term_pattern_for_linking = None
#          exclude_pattern_for_linking = None
#          log.info("AUTO-LINKING: No headers discovered, linking hook will not perform replacements.")

#     # --- 3. Define and Register the Linking Hook ---
#     def auto_link_headers_hook(markdown_content, page, config, files):
#         """
#         This hook runs for each page's markdown content.
#         It uses the pre-compiled regex and discovered data to add links.
#         """
#         # Skip processing if discovery failed or found nothing
#         if not term_pattern_for_linking or not exclude_pattern_for_linking:
#             return markdown_content

#         processed_parts = []
#         last_end = 0
#         # Track terms linked on *this specific page* if linking only first occurrence
#         linked_on_this_page = set()

#         # Split content by excluded patterns (code, links, html)
#         for match in exclude_pattern_for_linking.finditer(markdown_content):
#             start, end = match.span()
#             text_segment = markdown_content[last_end:start] # Process text *before* excluded part

#             # Apply term replacement within the safe segment
#             # Pass necessary data to the replacement helper function
#             processed_segment = term_pattern_for_linking.sub(
#                 lambda m: _replace_header_link_match(m, page, discovered_link_data, linked_on_this_page),
#                 text_segment
#             )
#             processed_parts.append(processed_segment)
#             processed_parts.append(match.group(0)) # Append the excluded part unchanged
#             last_end = end

#         # Process the final segment after the last excluded part
#         final_segment = markdown_content[last_end:]
#         processed_final_segment = term_pattern_for_linking.sub(
#             lambda m: _replace_header_link_match(m, page, discovered_link_data, linked_on_this_page),
#             final_segment
#         )
#         processed_parts.append(processed_final_segment)

#         # Join all parts back together
#         return "".join(processed_parts)

#     # Register the hook function *if* we have terms to link
#     if discovered_link_data:
#          env.page_markdown_hook = auto_link_headers_hook
#          log.info("AUTO-LINKING: Registered 'page_markdown_hook' for header linking.")
#     else:
#          # Ensure hook is None if no data (important for 'serve' reloads)
#          env.page_markdown_hook = None
#          log.info("AUTO-LINKING: No terms discovered, 'page_markdown_hook' not registered.")

#     log.info("AUTO-LINKING: define_env finished.")


# # --- Replacement Helper Function ---
# # Needs access to discovered_link_data, SCAN_DIR_FOR_HEADERS, CASE_SENSITIVE, LINK_FIRST_OCCURRENCE_ONLY
# # Defined globally for simplicity, could be nested if preferred (passing data explicitly)
# def _replace_header_link_match(match, page, link_data, linked_on_this_page):
#     """
#     Called by re.sub for each potential match. Creates the link if appropriate.
#     """
#     matched_text = match.group(1) # The actual text found in the markdown
#     # Key for dictionary lookup, depends on case sensitivity setting
#     term_key = matched_text if CASE_SENSITIVE else matched_text.lower()

#     # Check if the matched text corresponds to a discovered header
#     if term_key in link_data:
#         # Retrieve the pre-calculated data: ('DEM', 'elevation', 'ELEVATION')
#         filename_stem, slug, original_header_text = link_data[term_key]
#         # Use the text actually found in the current document as the link text
#         link_display_text = matched_text

#         # --- Avoid self-linking ---
#         # Construct the target file path relative to docs_dir
#         target_file_from_docs = Path(SCAN_DIR_FOR_HEADERS) / f"{filename_stem}.md"
#         target_file_norm = target_file_from_docs.as_posix() # Normalize for comparison
#         # Get current page path relative to docs_dir
#         current_page_path_from_docs = Path(page.file.src_uri).as_posix()
#         # Compare paths
#         if current_page_path_from_docs == target_file_norm:
#             return link_display_text # Don't link if it's the same file

#         # --- Check first occurrence logic ---
#         should_link = True
#         if LINK_FIRST_OCCURRENCE_ONLY:
#             page_term_tuple = (page.file.src_uri, term_key) # Unique key for this term on this page
#             if page_term_tuple in linked_on_this_page:
#                 should_link = False # Already linked this term on this page
#             else:
#                 linked_on_this_page.add(page_term_tuple) # Mark as linked for this page

#         # --- Create link if needed ---
#         if should_link:
#             # Calculate the relative path from the current page's directory to the target file
#             current_dir = Path(current_page_path_from_docs).parent
#             # Use the normalized target file path relative to docs dir
#             relative_path = os.path.relpath(target_file_norm, start=current_dir)
#             # Ensure forward slashes for the web link
#             relative_path = Path(relative_path).as_posix()

#             # Construct the final Markdown link: [Text](relative/path/File.md#slug)
#             final_link = f'[{link_display_text}]({relative_path}#{slug})'
#             log.debug(f"AUTO-LINKING: Linking '{link_display_text}' to '{relative_path}#{slug}' on page '{page.file.src_uri}'")
#             return final_link
#         else:
#             # Not linking (e.g., not first occurrence), return the original text
#             return link_display_text
#     else:
#         # Text matched regex but wasn't in our final dictionary (shouldn't happen)
#         return matched_text # Return original text as a safeguard