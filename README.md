# Modeling Intro

Welcome to the first coding repository for CMSE 802.

At first glance, this repository appears to be about drawing a colorful triangle. In reality, it is about something much more important; **how research software evolves**.

The triangle gives us a small, visual example that we can understand completely. Because the example is simple, we can focus our attention on the software instead of getting lost in complicated mathematics or domain-specific details.

Over the next few notebooks, you will start with a working script and gradually transform it into a reusable software tool. Along the way, we will explore many of the same practices used in larger scientific software projects.

## A model of models

Throughout this course, we will discuss three common components found in computational models:

- Analytical
- Physical
- Data-Driven

These are not separate categories. Most real-world research projects contain some mixture of all three.

For example:

Analytical components may include:

- equations
- symbolic mathematics
- optimization objectives
- mathematical constraints

Physical components may include:

- simulation
- finite differences
- iterative processes
- numerical methods

Data-driven components may include:

- parameter fitting
- statistics
- machine learning
- artificial intelligence

One way to think about a model is as a combination of these three ingredients.

We can represent that idea mathematically:

$$A + P + D = 1$$

where:

$A =$ Analytical contribution    
$P =$ Physical contribution  
$D =$ Data-Driven contribution   

and all three values are nonnegative.

## Why a Triangle?

A triangle provides a convenient way to visualize mixtures of three components.

In this repository we use color as a visual metaphor:

* Red   -> Analytical
* Green -> Physical
* Blue  -> Data-Driven

Every location inside the triangle represents a different combination of these three components.

- A point near the red corner represents a model with a strong analytical component.

- A point near the green corner represents a model with a strong physical component.

- A point near the blue corner represents a model with a strong data-driven component.

- A point near the center contains some mixture of all three.

We will be introdcing a lot of modeling methods and techniques. Later in the semester we will think about how these models fall in our trinagle. 

[Insert Example Triangle Figure Here]

## Why Start Here?

Many students enter graduate school with some programming experience, but relatively little experience thinking about software as an evolving artifact.

A common pattern in research looks something like:

    Idea
      ↓
    Quick Script
      ↓
    Working Script
      ↓
    Reusable Functions
      ↓
    Library
      ↓
    Research Tool

This repository follows that progression.

Rather than building a large project from scratch, we will use a small example to practice the habits that support high-quality research software.

## Sceintific Software Engineering Principles

Throughout CMSE 802 we will revisit five qualities of scientific software:

- Safe
- Portable
- Reproducible
- Robust
- Literate

You do not need to master all of these ideas immediately.

Instead, use them as a lens when evaluating software and making design decisions.

When you modify code, ask:

- Does this make the code safer?
- Does this make the code easier to move to another machine?
- Does this make results easier to reproduce?
- Does this make the software more robust?
- Does this make the code easier for another person to understand?

The exercises in this repository are designed to make those questions concrete.

# Learning Goals

By the end of this repository, you should be able to:

- run and inspect existing code
- make small improvements without breaking functionality
- replace magic numbers with meaningful variables
- refactor a script into reusable functions
- design useful function arguments and defaults
- move functionality into a Python module
- import and reuse code from multiple notebooks
- use Git to track software evolution
- improve code quality using automated tools
- explain how software engineering supports scientific research

# Repository Structure

## Notebook 01: Model Triangle

Start with a working script that generates a barycentric RGB triangle. You will explore the code, make modifications, and practice improving an existing program.

## Notebook 02: Building a Library

Refactor the original script into a reusable Python module.

Topics include:

- functions
- imports
- code reuse
- organization

## Notebook 03: Improving Software

Introduce tools that help improve software quality.

Topics include:

- Git
- Ruff
- formatting
- software improvement workflows

## SUGGESTED LEARNING FLOW

Work through the notebooks in order.

1. Run and modify a working script.
2. Transform the script into a reusable library.
3. Improve the library using software engineering tools.

Each notebook builds on the work completed in the previous notebook.

# Optional Quick Start

An ```enviornment.yml``` file is included so you can create a repository with all of the necessary files.  This particular repository only uses ```numpy```, ```matplotlib``` and ```ruff```.  You may not need to install anything. However you can use the following command to create the environment:

```bash
conda env create -f environment.yml
```

# Notes for students

As you work through the repository:

- Keep changes small.
- Test frequently.
- Run your code after each modification.
- Use Git commits to capture important milestones.
- Focus on understanding why a change is useful, not just how to make it.
- Discuss design decisions with your teammates.

Most importantly:

- Start with code that works.
- Improve it in small steps.
- Preserve behavior while improving readability, reuse, and portability.

