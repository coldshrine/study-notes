# [Managing The Development of Large Software Systems](http://www-scf.usc.edu/~csci201/lectures/Lecture11/royce1970.pdf)

The context for this paper was related with the development of software packages for spacecraft mission planning, commanding and post-flight analysis.

There are two essential steps of computer programs regardless of the size or complexity: Analysis and coding. However, manufacturing large software projects taking into account only these steps ia doomed to failure.

A more grandiose approach precedes two levels of requirement analysis, separated by a design step and followed by a testing step. These steps are separated because they are planned and staffed differently in terms of resources.

    System Requirements
        ↘
        Software Requirements
            ↘
            Analysis
                ↘
                Program Design
                    ↘
                    Coding
                        ↘
                        Testing
                            ↘
                            Operations

The iterative relationship between phases can be reflected in the following scheme. Each step progresses and the design is further detailed.

Hopefully the interaction is confined in successive steps:

    System Requirements
        ↖  ↘
        Software Requirements
            ↖  ↘
            Analysis
                ↖  ↘
                Program Design
                    ↖  ↘
                    Coding
                        ↖  ↘
                        Testing
                            ↖  ↘
                            Operations

The problem is that design iterations are never confined to successive steps:

    System Requirements
        ↘
     ┌► Software Requirements
     │      ↘
     │      Analysis
     │          ↘
     └───────── Program Design ──┐
                    ↘            │
                    Coding       │
                        ↘        │
                        Testing ◄┘
                            ↘
                            Operations

## Step 1: Program design come first

A first step towards fixing the previous problem is to introduce a preliminary program design step between the software requirements and analysis phase. Critics can argue about the program designer being forced to design in a vacuum of software requirements without any analysis, and that the preliminary design may result in substantial error; and that would be correct, but it would miss the point. This is intended to assure the software won't fail because of storage, timing or data flux reasons. As analysis proceeds, collaboration must happen between the program designer and the analyst, so proper allocation of execution time and storage resources happens.

    ┌─────┐        ┌─► Document System Overview
    └─────┘        ├─► Design Database and Processors
        ↘          ├─► Allocate Subrutine Storage
        ┌─────┐    ├─► Allocate Subrutine Execution Times
        └─────┘    ├─► Describe Operating Procedures
            ↘      │
            Preliminary Program Design
                ↘
                ┌─────┐
                └─────┘
                    ↘
                    ┌─────┐
                    └─────┘

The procedure is made from these steps:
1. Begin the design with program designers, not analysts or programmers.