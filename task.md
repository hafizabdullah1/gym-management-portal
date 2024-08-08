https://awake-attack-6b0.notion.site/Gym-APP-269b34b5e6de4422af73de6273f5465e

# Gym APP

<!-- **Synopsis** -->
### Synposis

We need a Gym management portal for gym manager so he can enter members, manage their deadlines for fee and overall reports. Detail requirements are shared in next sections

**Members**

Every member will have following features

- Name
- Phone number
- Fee amount
- Fee date
- picture (for taking picture, it should activate the camera)
- Status (Active/Non Active)

**Dashboard**

Dashboard should show the main 3 sections

- Members
- Reports
- Members sorted by due date

**Reports**

Reports should give a date filter to select start date and end date. And once user has selected it should show total revenue generated between those two dates.

Basically there is a 30 days cycle for every member. For example if a member submits fee on 13th of every month. Once he submits the fee, gym admin will mark it as paid and his money will be added to included in the calculations of report. 2 days before 13 of next month, it will change the status from **paid** to **due** and it will start showing up in the list of members having payment due