# Report

## Activity Overview
For this project, I integrated a continuous integration system through GitHub Actions. I also added a forensics logger to that workflow, then modified some functions in the source code to check the logger. Finally, I created a fuzz.py file, also run with the CI system, to test some functions in the source code. Some example screenshots for output are labeled and included in the base directory.

### Continuous Integration with GitHub Actions
I hadn't used this feature before, so it took some getting used to. However, when the syntax clicked, it was much easier than other projects I've worked on to see what implication the recent changes have. I made one workflow for the CI portion that triggers on push and pull requests, which also runs fuzz.py. When running fuzz.py, I specifically mentioned to the workflow that it shouldn't crash when it hits an error, since I felt the whole CI check should run, then display a summary of errors. I made a different workflow for the forensics logger, so that responsibilities were kept separate and easier to diagnose.

### Logging Statements for Forensics
As mentioned above, I accomplished this through a second workflow in GitHub actions that triggered whenever it saw a push request. When it sees a commit, it logs the files changed, the commit number, and other relevant information inside the logs. These are accessible through the job history in the Actions area, under the "Log File Modifications" tab. After figuring out the Actions system through the CI portion, this was fairly straightforward; the biggest difference between the two was the goal of the workflow, but the implementation followed a similar structure.

### Fuzzing 5 Python Methods
This portion was also included within the standard CI workflow, so it was fairly easy to include in the Actions workflow. For this, I decided to import the functions to my fuzz.py file, then run them on some sample inputs. This was harder than I expected, since I had to use the dynamic method to import the functions (due to a subfolder having the "-" symbol in its name, which isn't allowed normally). Now, whenever the normal CI Action is triggered, this fuzzing will also take place and display the result of the testing inside the job history in the Actions tab. I wasn't too familiar with the unittest methods, but I found them quite intuitive after I understood them, so I will use this in my future projects.

## Screenshot/Log Guide:
The logs are created and stored in the Actions section under job history. The fuzz test results will be under the CI workflow, and the forensics modification logs will be under the Log File Modifications section.
For the screenshots, the example_fuzz photos show some sample output from the tester that runs during the CI workflow. The exampleLogging+Integration photo displays a sample history of both the CI and Log File Modification workflows that run on each commit. The exampleCISnippet photo displays the first few sections of the execution history of the CI Action workflow.
