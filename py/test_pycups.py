import json
import time

import os

print(json.dumps(dict(os.environ), indent=4))

import cups

'''
export PYCUPS_DEBUG=1
'''
def get_title(name='Python_Status_print'):
    timestr = time.strftime("%Y%m%d-%H.%M.%S")
    return '%s-%s' %(name, timestr)


# def get_datetime_stamp():
#     return time.strftime("%Y%m%d %H:%M:%S")

# def get_title():
#     datetime_stamp = get_datetime_stamp()
#     title = '%s pk[%s], date[%s]' % ('model_name', 'self.patient_forms.pk', datetime_stamp)
# 
#     return title

conn = cups.Connection()

# title= get_title()
# 
# print(title)

'''
def printFile(printer, filename, title, options)
printFile(printer, filename, title, options) -> integer

Print a file.

@type printer: string  @param printer: queue name python
@type filename: string @param filename: local file path to the document
@type title: string    @param title: title of the print job
@type options: dict    @param options: dict of options
@return: job ID        @raise IPPError: IPP problem
'''

# job_ID = conn.printFile('Brother-MFC-L2707DW', '/home/tangc/tmp/t.txt', get_title(), {})
# print(job_ID)

requested_attributes = [
    'job_id',

    'job-originating-user-name',

    'job-printer-state-message', 'time-at-completed', 'time-at-processing',
    'job-sheets', 'job-k-octets', 'document-count', 'job-media-progress',
    'job-uri', 'job-media-sheets-completed', 'job-more-info', 'job-originating-user-name',
    'job-printer-up-time', 'time-at-creation', 'job-printer-uri', 'job-preserved',
    'job-state-reasons', 'job-state', 'job-originating-host-name', 'job-name', 'job-priority',
    'document-format', 'job-uuid', 'printer-uri', 'job-printer-state-reasons', 'job-hold-until']


def test_getJobs():
    '''
    def getJobs(
        which_jobs='not_completed',
        my_jobs=False,
        limit=_1,
        first_job_id=_1,
        requested_attributes=None)
    
    getJobs(which_jobs='not-completed', my_jobs=False, limit=-1, first_job_id=-1, requested_attributes=None)
     -> dict Fetch a list of jobs.
        @type which_jobs: string @param which_jobs: which jobs to fetch; possible values: 'completed', 'not-completed', 'all'
        @type my_jobs: boolean @param my_jobs: whether to restrict the returned jobs to those owned by the current CUPS user (as set by L{cups.setUser}).
        @type limit: integer @param limit: maximum number of jobs to return
        @type first_job_id: integer @param first_job_id: lowest job ID to return @type requested_attributes: string list @param requested_attributes: list of requested attribute names
    
        @return: a dict, indexed by job ID, of dicts representing job attributes.
        @raise IPPError: IPP problem
    '''
    _jobs = conn.getJobs(which_jobs='all', #first_job_id=12, limit=1 ,
        requested_attributes=requested_attributes
        # requested_attributes= # ['job_id', "job-printer-state-reasons", "job-printer-up-time"]
    
    ) #, first_job_id=3, limit=1)
    
    print(json.dumps(_jobs, indent=4))
    