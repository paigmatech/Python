import os
import re

# Directory containing Python scripts
SCRIPTS_DIR = "c:/Users/lenovo/Documents/GitHub/Python/Scripts"  # Update this path to your scripts directory
BLOG_POSTS_DIR = "c:/Users/lenovo/Documents/GitHub/Python/BlogPosts"  # Update this path to your blog posts directory

# Template for the blog post
BLOG_POST_TEMPLATE = """
---
title: "{title}"
date: "{date}"
description: "{description}"
---

## Introduction
{introduction}

## Key Code Snippets
```python
{code_snippets}