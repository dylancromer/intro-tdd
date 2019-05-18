# intro-tdd
Introduction to TDD, in a research context. Heavily Inspired by Gary Bernhardt

## What is TDD?

Test-driven development, or TDD, is the practice of writing code using the following formula:

- Write a test for the code you want to write, but that doesn't exist yet. This test is a short program that tries to use pieces of the not-yet-existing code.
  - This test will fail. It *must* fail.
- Write the minimal amount of code needed to cause the test you just wrote to pass.
- Refactor your code, removing inefficiencies, cleaning up names, etc.
- Repeat as needed until your code is done.
