from nanohttp import HTTPKnownStatus, settings


class StatusRoomMemberAlreadyExist(HTTPKnownStatus):
    status = '810 Already Added To Target'


class StatusRoomMemberNotFound(HTTPKnownStatus):
    status = '807 User Not Found'


class StatusChatServerNotFound(HTTPKnownStatus):
    status = '806 Chat Server Not Found'


class StatusChatRoomNotFound(HTTPKnownStatus):
    status = '808 Chat Room Not Found'


class StatusChatServerNotAvailable(HTTPKnownStatus):
    status = '800 Chat Server Not Available'


class StatusChatInternallError(HTTPKnownStatus):
    status = '801 Chat Server Internal Error'


class StatusChatRoomMemberNotFound(HTTPKnownStatus):
    status = '805 Chat Room Member Not Found'


class StatusNotAMember(HTTPKnownStatus):
    status = '617 Not A Member'


class StatusOutOfLimitRoomSubscription(HTTPKnownStatus):
    status = '804 Number Of Chat Room Subscription Is Out Of Limit'


class StatusRoomAlreadyExists(HTTPKnownStatus):
    status = '615 Room Already Exists'


class StatusMaximumSubscribeAtRoom(HTTPKnownStatus):
    def __init__(self, maximum_room_subscription):
        self.status = f'716 Maximum {maximum_room_subscription} Rooms To ' \
                      f'Subscribe At A Time'


class MemberAlreadyAddedToTarget(HTTPKnownStatus):
    status = '604 Member Already Added To Target'


class StatusCASServerNotFound(HTTPKnownStatus):
    status = '811 CAS Server Not Found'


class StatusCASServerNotAvailable(HTTPKnownStatus):
    status = '802 CAS Server Not Available'


class StatusCASServerInternalError(HTTPKnownStatus):
    status = '803 CAS Server Internall Error'


class StatusInvalidApplicationID(HTTPKnownStatus):
    status = '620 Invalid Application ID'


class StatusInvalidSecret(HTTPKnownStatus):
    status = '621 Invalid Secret'


class StatusRepetitiveTitle(HTTPKnownStatus):
    status = '600 Repetitive Title'


class StatusTokenExpired(HTTPKnownStatus):
    status = '627 Token Expired'


class StatusMalformedToken(HTTPKnownStatus):
    status = '626 Malformed Token'


class StatusAlreadyInThisOrganization(HTTPKnownStatus):
    status = '628 Already In This Organization'


class StatusNotInThisOrganization(HTTPKnownStatus):
    status = '400 Not In This Organization'


class StatusAlreadyTagAdded(HTTPKnownStatus):
    status = '634 Already Tag Added'


class StatusAlreadyTagRemoved(HTTPKnownStatus):
    status = '635 Already Tag Removed'


class StatusNotSubscribedIssue(HTTPKnownStatus):
    status = '637 Not Subscribed Issue'


class StatusRelatedIssueNotFound(HTTPKnownStatus):
    def __init__(self, related_issue_id):
        self.status = f'647 relatedIssue With Id {related_issue_id} Not Found'


class StatusResourceNotFound(HTTPKnownStatus):
    def __init__(self, resource_id):
        self.status = f'609 Resource not found with id: {resource_id}'


class StatusIssueBugMustHaveRelatedIssue(HTTPKnownStatus):
    status = '649 The Issue Bug Must Have A Related Issue'


class StatusManagerNotFound(HTTPKnownStatus):
    status = '608 Manager Not Found'


class StatusSecondaryManagerNotFound(HTTPKnownStatus):
    status = '650 Secondary Manager Not Found'


class StatusLaunchDateMustGreaterThanCutoffDate(HTTPKnownStatus):
    status = '651 The Launch Date Must Greater Than Cutoff Date'


class StatusIssueNotFound(HTTPKnownStatus):
    def __init__(self, issue_id=None):
        # This + between strings are decided by PyLover.
        # DO NOT DO THAT ANYWHERE
        self.status = f'605 Issue Not Found' + \
                      (f': {issue_id}' if issue_id is not None else '')


class StatusMemberNotFound(HTTPKnownStatus):
    status = '610 Member Not Found'


class StatusAlreadyAddedToGroup(HTTPKnownStatus):
    status = '652 Already Added To Group'


class StatusMemberNotExistsInGroup(HTTPKnownStatus):
    status = '653 Member Not Exists In Group'


class StatusAlreadyGrantedSpecialty(HTTPKnownStatus):
    status = '655 Specialty Already Granted'


class StatusSpecialtyNotGrantedYet(HTTPKnownStatus):
    status = '656 Specialty Not Granted Yet'


class StatusRepetitiveOrder(HTTPKnownStatus):
    status = '615 Repetitive Order'


class StatusSpecialtyNotFound(HTTPKnownStatus):
    status = '645 Specialty Not Found'


class StatusGroupNotFound(HTTPKnownStatus):
    status = '659 Group Not Found'


class StatusEventTypeNotFound(HTTPKnownStatus):
    status = '658 Event Type Not Found'


class StatusEndDateMustBeGreaterThanStartDate(HTTPKnownStatus):
    status = '657 End Date Must Be Greater Than Start Date'


class StatusInvalidStartDateFormat(HTTPKnownStatus):
    status = '791 Invalid Start Date Format'


class StatusInvalidEndDateFormat(HTTPKnownStatus):
    status = '790 Invalid End Date Format'


class StatusLimitedCharecterForNote(HTTPKnownStatus):
    status = '902 At Most 1024 Characters Are Valid For Note'


class StatusInvalidEstimatedHoursType(HTTPKnownStatus):
    status = '900 Invalid Estimated Hours Type'


class StatusSummaryNotInForm(HTTPKnownStatus):
    status = '799 Summary Not In Form'


class StatusFormNotAllowed(HTTPKnownStatus):
    status = '709 Form Not Allowed'


class StatusReleaseNotFound(HTTPKnownStatus):
    status = '607 Release Not Found'


class StatusInvalidReleaseIdType(HTTPKnownStatus):
    status = '750 Invalid Release Id Type'


class StatusInvalidStagesValue(HTTPKnownStatus):
    def __init__(self, stages_values):
        self.status = f'705 Invalid stage value, only one of ' \
                      f'"{", ".join(stages_values)}" will be accepted'


class StatusInvalidStatusValue(HTTPKnownStatus):
    def __init__(self, statuses_values):
        self.status = f'705 Invalid status value, only one of ' \
                      f'"{", ".join(statuses_values)}" will be accepted'


class StatusProjectNotFound(HTTPKnownStatus):
    status = '601 Project Not Found'


class StatusHiddenProjectIsNotEditable(HTTPKnownStatus):
    status = '746 Hidden Project Is Not Editable'


class StatusPhaseNotFound(HTTPKnownStatus):
    status = '613 Phase Not Found'


class StatusInvalidWorkflowIdType(HTTPKnownStatus):
    status = '743 Invalid Workflow Id Type'


class StatusWorkflowNotFound(HTTPKnownStatus):
    status = '616 Workflow Not Found'


class StatusInvalidRoleValue(HTTPKnownStatus):
    status = '756 Invalid Role Value'


class StatusMaxLenghtForTitle(HTTPKnownStatus):

    def __init__(self, lenght):
        self.status = f'704 At Most {lenght} Characters Are Valid For Title'


class StatusEventTypeIdIsNull(HTTPKnownStatus):
    status = '798 Event Type Id Is Null'


class StatusMaxLenghtForDescription(HTTPKnownStatus):
    def __init__(self, lenght):
        self.status = f'703 At Most {lenght} Characters Are Valid For ' \
                      'Description'


class StatusTitleNotInForm(HTTPKnownStatus):
    status = '710 Title Not In Form'


class StatusEndDateNotInForm(HTTPKnownStatus):
    status = '793 End Date Not IN Form'


class StatusStartDateNotInForm(HTTPKnownStatus):
    status = '792 Start Date Not In Form'


class StatusEndDateNotInForm(HTTPKnownStatus):
    status = '793 End Date Not In Form'


class StatusEstimatedHoursNotInForm(HTTPKnownStatus):
    status = '901 Estimated Hours Not In Form'


class StatusNoteIsNull(HTTPKnownStatus):
    status = '903 Note Is Null'


class StatusEstimatedHoursIsNull(HTTPKnownStatus):
    status = '904 Estimated Hours Is Null'


class StatusStartDateIsNull(HTTPKnownStatus):
    status = '905 Start Date Is Null'


class StatusEndDateIsNull(HTTPKnownStatus):
    status = '906 End Date Is Null'


class StatusRepeatNotInForm(HTTPKnownStatus):
    status = '911 Repeat Not In Form'


class StatusQueryParameterOrQueryString(HTTPKnownStatus):
    status = '912 Query Parameter Not In Form Or Query String'


class StatusHoursMustBePositive(HTTPKnownStatus):
    status = '914 Hours Must Be Positive'


class StatusHoursExceedsTheLimit(HTTPKnownStatus):
    status = '916 Hours Exceeds The Limit'


class StatusTypeIdNotInForm(HTTPKnownStatus):
    status = '794 Type Id Not In Form'


class StatusInvalidOrderType(HTTPKnownStatus):
    status = '741 Invalid Order Type'


class StatusInvalidSpecialtyIdType(HTTPKnownStatus):
    status = '788 Invalid Specialty Id Type'


class StatusOrderNotInForm(HTTPKnownStatus):
    status = '742 Order Not In Form'


class StatusInvalidTargetIssueIdType(HTTPKnownStatus):
    status = '781 Invalid Target Issue Id Type'


class StatusTargetIssueIdNotInForm(HTTPKnownStatus):
    status = '780 Target Issue Id Not In Form'


class StatusTargetIssueIdIsNull(HTTPKnownStatus):
    status = '779 Target Issue Id Is Null'


class StatusInvalidTitleFormat(HTTPKnownStatus):
    status = '747 Invalid Title Format'


class StatusInvalidMemberIdType(HTTPKnownStatus):
    status = '736 Invalid Member Id Type'


class StatusMemberIdNotInForm(HTTPKnownStatus):
    status = '735 Member Id Not In Form'


class StatusMemberIdIsNull(HTTPKnownStatus):
    status = '774 Member Id Is Null'


class StatusInvalidProjectIdType(HTTPKnownStatus):
    status = '714 Invalid Project Id Type'


class StatusProjectIdNotInForm(HTTPKnownStatus):
    status = '713 Project Id Not In Form'


class StatusAuthorizationCodeNotInForm(HTTPKnownStatus):
    status = '762 Authorization Code Not In Form'


class StatusInvalidOrganizationIdType(HTTPKnownStatus):
    status = '763 Invalid Organization Id Type'


class StatusInvalidEventTypeIdValue(HTTPKnownStatus):
    status = '789 Invalid Event Type Id Value'


class StatusOrganizationIdNotINForm(HTTPKnownStatus):
    status = '761 Organization Id Not In Form'


class StatusOrganizationIdNotFound(HTTPKnownStatus):
    status = '760 Organization Id Not Found'


class StatusOrganizationIdIsNull(HTTPKnownStatus):
    status = '771 Organization Id Is Null'


class StatusTokenNotInForm(HTTPKnownStatus):
    status = '757 Token Not In Form'


class StatusRedirectUriNotInForm(HTTPKnownStatus):
    status = '766 Redirect Uri Not In From'


class StatusApplicationIdNotInForm(HTTPKnownStatus):
    status = '764 Application Id Not In Form'


class StatusScopesNotInForm(HTTPKnownStatus):
    status = '765 Scopes Not In Form'


class StatusInvalidEmailFormat(HTTPKnownStatus):
    status = '400 Invalid Email Format'


class StatusInvalidPhaseIdType(HTTPKnownStatus):
    status = '738 Invalid Phase Id Type'


class StatusPhaseIdNotInForm(HTTPKnownStatus):
    status = '737 Phase Id Not In Form'


class StatusInvalidCutoffFormat(HTTPKnownStatus):
    status = '702 Invalid Cutoff Format'


class StatusCutoffNotInForm(HTTPKnownStatus):
    status = '712 Cutoff Not In Form'


class StatusFileNotInForm(HTTPKnownStatus):
    status = '758 File Not In Form'


class StatusPhaseIdIsNull(HTTPKnownStatus):
    status = '770 Phase Id Is Null'


class StatusInvalidResourceIdType(HTTPKnownStatus):
    status = '716 Invalid Resource Id Type'


class StatusResourceIdNotInForm(HTTPKnownStatus):
    status = '715 Resource Id Not In Form'


class StatusResourceIdIsNull(HTTPKnownStatus):
    status = '769 Resource Id Is Null'


class StatusStatusNotInForm(HTTPKnownStatus):
    status = '719 Status Not In Form'


class StatusInvalidDaysType(HTTPKnownStatus):
    status = '721 Invalid Days Type'


class StatusInvalidDueDateFormat(HTTPKnownStatus):
    status = '701 Invalid Due Date Format'


class StatusManagerReferenceIdNotInForm(HTTPKnownStatus):
    status = '777 Manager Reference Id Not In Form'


class StatusManagerReferenceIdIsNull(HTTPKnownStatus):
    status = '778 Manager Reference Id Is Null'


class StatusInvalidLaunchDateFormat(HTTPKnownStatus):
    status = '784 Invalid Launch Date Format'


class StatusLaunchDateNotInForm(HTTPKnownStatus):
    status = '783 Launch Date Not In Form'


class StatusInvalidGroupIdType(HTTPKnownStatus):
    status = '797 Invalid Group Id Type'


class StatusGroupIdNotInForm(HTTPKnownStatus):
    status = '795 Group Id Not In Form'


class StatusGroupIdIsNull(HTTPKnownStatus):
    status = '796 Group Id Is Null'


class StatusManagerIdNotInForm(HTTPKnownStatus):
    status = '786 Manager Id Not In Form'


class StatusManagerIdIsNull(HTTPKnownStatus):
    status = '785 Manager Id Is Null'


class StatusIssueIdIsNull(HTTPKnownStatus):
    status = '775 Issue Id Is Null'


class StatusInvalidIssueIdType(HTTPKnownStatus):
    status = '722 Invalid Issue Id Type'


class StatusDaysNotInForm(HTTPKnownStatus):
    status = '720 Days Not In Form'


class StatusKindNotInForm(HTTPKnownStatus):
    status = '718 Kind Not In Form'


class StatusDueDateNotInForm(HTTPKnownStatus):
    status = '711 Due Date Not In Form'


class StatusPriorityNotInForm(HTTPKnownStatus):
    status = '768 Priority Not In Form'


class StatusInvalidPriority(HTTPKnownStatus):
    def __init__(self, issue_priorities):
        self.status = f'767 Invalid priority, only one of ' \
                      f'"{", ".join(issue_priorities)}" will be accepted'


class StatusInvalidKind(HTTPKnownStatus):
    def __init__(self, issue_kinds):
        self.status = f'717 Invalid kind, only one of ' \
                      f'"{", ".join(issue_kinds)}" will be accepted'


class StatusInvalidHoursType(HTTPKnownStatus):
    status = '915 Invalid Hours Type'


class StatusHoursNotInForm(HTTPKnownStatus):
    status = '929 Hours Not In Form'


class StatusNoteNotInForm(HTTPKnownStatus):
    status = '930 Note Not In Form'


class StatusInvalidDatePeriod(HTTPKnownStatus):
    status = '664 Invalid Date Period'


class StatusDailyReportAlreadyExist(HTTPKnownStatus):
    status = '665 Daily Report Already Exist'


class StatusInvalidDateFormat(HTTPKnownStatus):
    status = '400 Invalid Date Format'


class StatusDateNotInForm(HTTPKnownStatus):
    status = '931 Date Not In Form'


class StatusIssueIdNotInForm(HTTPKnownStatus):
    status = '723 Issue Id Not In Form'


class StatusItemIsAlreadyApproved(HTTPKnownStatus):
    status = '666 Item Is Already Approved'


class StatusInvalidBatchToAppendIssue(HTTPKnownStatus):
    status = '667 Invalid Batch To Append Issue'


class StatusInvalidSkillIdType(HTTPKnownStatus):
    status = '941 Invalid Skill Id Type'


class StatusSkillNotFound(HTTPKnownStatus):
    status = '942 Skill Not Found'


class StatusSkillIdIsNull(HTTPKnownStatus):
    status = '945 Skill Id Is Null'


class StatusSkillIdNotInForm(HTTPKnownStatus):
    status = '946 Skill Id Not In Form'


class StatusTheMimetypeDoesNotMatchTheFileType(HTTPKnownStatus):
    status = '710 The Mimetype Does Not Match The File Type'


class StatusAlreadyGrantedRole(HTTPKnownStatus):
    status = '668 Already Granted Role'


class StatusRoleNotGrantedYet(HTTPKnownStatus):
    status = '669 Role Not Granted Yet'


class StatusInvalidRoleValue(HTTPKnownStatus):
    status = '947 Invalid Role Value'


class StatusRoleIsNull(HTTPKnownStatus):
    status = '948 Role Is Null'


class StatusRoleNotInForm(HTTPKnownStatus):
    status = '949 Role Not In Form'


class StatusAttachmentAlreadyDeleted(HTTPKnownStatus):
    status = '629 Attachment Already Deleted'


class StatusParameterExistsInTheForm(HTTPKnownStatus):
    status = '708 No Parameter Exists In The Form'


class StatusInvalidBatchTitleType(HTTPKnownStatus):
    status = '937 Invalid Batch Title Type'


class StatusThisProjectDoseNotHaveThisBatch(HTTPKnownStatus):
    status = '938 This Project Dose Not Have This Batch'


class StatusAlreadyRemovedThisProjectWithBatch(HTTPKnownStatus):
    status = '940 Already Removed This Project With Batch'


class StatusInvalidBatchMinimum(HTTPKnownStatus):
    status = '943 Invalid Batch Less Than 1'


class StatusInvalidBatchMaximum(HTTPKnownStatus):
    status = '936 Invalid Batch More Than 99'


class StatusBatchTitleNotInForm(HTTPKnownStatus):
    status = '944 Batch Title Not In Form'


class StatusLinkAlreadyDeleted(HTTPKnownStatus):
    status = '629 Link Already Deleted'


class StatusURLRequired(HTTPKnownStatus):
    status = '950 URL Is Required'


class StatusURLIsNull(HTTPKnownStatus):
    status = '951 URL Is Null'


class StatusURLInvalidLength(HTTPKnownStatus):
    status = '952 URL Invalid Length'


class StatusMemberNotInGroup(HTTPKnownStatus):
    status = '670 Member Not In Group'


class StatusIsDoneNotInForm(HTTPKnownStatus):
    status = '953 Is Done Not In Form'


class StatusInvalidProjectBatchToAppendIssue(HTTPKnownStatus):
    status = '671 Invalid Project Batch To Append Issue'


class StatusInvalidMemberItem(HTTPKnownStatus):
    status = '672 Selected Item Belongs to Another Member'


class StatusCantCreateDailyReportForNoEstimatedItem(HTTPKnownStatus):
    status = '673 Cant Create Daily Report For No Estimated Item'


class StatusEstimatedHoursMustBeGreaterThanZero(HTTPKnownStatus):
    status = '954 Estimated Hours Must Be Greater Than Zero'


class StatusDescriptionNotInForm(HTTPKnownStatus):
    status = '955 Description Not In Form'


class StatusModuleNotInForm(HTTPKnownStatus):
    status = '957 Module Not In Form'


class StatusModuleIsNull(HTTPKnownStatus):
    status = '958 Module Is Null'


class StatusAccessLevelAlreadyExist(HTTPKnownStatus):
    status = '960 Access Level Already Exist'


class StatusAlreadyIncludesAssignedTasks(HTTPKnownStatus):
    status = '961 Already Includes Assigned Tasks'


class StatusAlreadyIncludesPhases(HTTPKnownStatus):
    status = '962 Already Includes Phases'


class StatusAlreadyIncludesProjects(HTTPKnownStatus):
    status = '963 Already Includes Projects'


class StatusIsSkippedNotInForm(HTTPKnownStatus):
    status = '964 Is Skipped Not In Form'


class StatusIsSkippedIsNull(HTTPKnownStatus):
    status = '965 Is Skipped Is Null'


class StatusAddMemberToPublicGroup(HTTPKnownStatus):
    status = '400 Adding a Member to Public Groups Is not Allowed'


class StatusMemberHasItemRelatedToSpeciality(HTTPKnownStatus):
    status = '400 Removing Speciality of a Member who has an Item ' \
             'Related to that Speciality is not Allowed'


class StatusUpdateSpecialtySkill(HTTPKnownStatus):
    status = '400 Changing Skill of a Specialty Is not Allowed'


class StatusAlreadySkipped(HTTPKnownStatus):
    status = '966 Already Skipped'


class StatusTheEstimatedHoursBeLessThanHoursReported(HTTPKnownStatus):
    status = '967 The Estimated Hours Be Less Than Hours Reported'


class StatusTheReportedHoursBeMoreThanEstimatedHours(HTTPKnownStatus):
    status = '968 The Reported Hours Be More Than Estimated Hours'


class StatusSubscribeNotFound(HTTPKnownStatus):
    status = '969 Subscribe Not Found'


class StatusBatchAlreadyAppended(HTTPKnownStatus):
    status = '400 Batch Already Appended'


class StatusReleaseAlreadyCompleted(HTTPKnownStatus):
    status = '400 Release Already Completed'


class StatusMemberIsAlreadyKickedFromOrganization(HTTPKnownStatus):
    status = '400 Member Is Already Kicked From Organization'


class StatusRepetitiveLevel(HTTPKnownStatus):
    status = '400 Repetitive Level'


class StatusLevelNotInForm(HTTPKnownStatus):
    status = '400 Level Not In Form'


class StatusLevelIsNull(HTTPKnownStatus):
    status = '400 Level Is Null'


class StatusInvalidLevelIdType(HTTPKnownStatus):
    status = '400 Invalid Level Type'


class StatusAuditlogLevelIdNotInForm(HTTPKnownStatus):
    status = '400 AuditlogLevelId Not In Form'


class StatusAuditlogLevelIdIsNull(HTTPKnownStatus):
    status = '400 AuditlogLevelId Is Null'


class StatusInvalidAuditlogLevelIdType(HTTPKnownStatus):
    status = '400 Invalid AuditlogLevelId Type'


class StatusModelNameNotInForm(HTTPKnownStatus):
    status = '400 Model Name Not In Form'


class StatusModelNameIsNull(HTTPKnownStatus):
    status = '400 Model Name Is NULL'


class StatusAttributeNotInForm(HTTPKnownStatus):
    status = '400 Attribute Not In Form'


class StatusAttributeIsNull(HTTPKnownStatus):
    status = '400 Attribute Is NULL'


class StatusRepetitiveAuditlog(HTTPKnownStatus):
    status = '400 Repetitive Auditlog'


class StatusTitleLengthInvalid(HTTPKnownStatus):
    status = '400 Title Length Must Be Greater Than 3' \
             ' Characters and Less than 256 Character'


class StatusTheMemberHasNotThisSkill(HTTPKnownStatus):
    status = '400 The Member Has Not This Skill'


#####

class StatusInvalidStringType(HTTPKnownStatus):
    status = '400 invalid type for title'


class StatusTitleIsRequired(HTTPKnownStatus):
    status = '400 title field is required'


class StatusRepetitiveTitle(HTTPKnownStatus):
    status = '400 title is already exist'


class StatusTitleIsNull(HTTPKnownStatus):
    status = '400 title is null'


class StatusFirstnameIsNull(HTTPKnownStatus):
    status = '400 firstname field is null'


class StatusLastnameIsNull(HTTPKnownStatus):
    status = '400 lastname field is null'


class StatusGenderIsNull(HTTPKnownStatus):
    status = '400 gender field is null'


class StatusGenderIsRequired(HTTPKnownStatus):
    status = '400 gender field is Required'


class StatusEmailIsNull(HTTPKnownStatus):
    status = '400 email is null'


class StatusEmailIsRequired(HTTPKnownStatus):
    status = '400 Email Not In Form'


class StatusRepetitiveEmail(HTTPKnownStatus):
    status = '400 email address is already exist'


class HTTPIncorrectEmailOrPassword(HTTPKnownStatus):
    status = '400 Incorrect Email Or Password'


class HTTPTokenExpired(HTTPKnownStatus):
    status = '400 Token has been expired'


class HTTPMalformedToken(HTTPKnownStatus):
    status = '400 Malformed Token'


class HTTPPasswordNotInForm(HTTPKnownStatus):
    status = '400 Password Not In Form'


class HTTPPasswordIsNull(HTTPKnownStatus):
    status = '400 Password is null'


class HTTPPasswordInvalidLength(HTTPKnownStatus):
    status = '400 Invalid Password Length'


class HTTPPasswordWrongPattern(HTTPKnownStatus):
    status = '400 Password Not Complex Enough'
