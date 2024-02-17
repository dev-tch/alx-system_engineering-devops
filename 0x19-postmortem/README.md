#### Bug report for software called Logistar used in industry WMS

### Summary: 
on fevrier 01/02/2018 ; in  warehouse management system, the impression of etiquette, is not working.

### Timeline

- 00:00 FR: the operator in WMS can not print new etiquette for the preparation support 

- 08:00 FR: view the logrun of  function responisble of printing new  etiquette 

==> i found an error raised by the programming languague  (progress openedge 4gl)
==> error: 'Mismatched parameter types passed to procedure imprime_etiquette. (3230) '

- 08:30 FR: in my workspace i search all occuremnces of the keyword  'imprime_etiquett'
- 09:35 FR: i found 5 calls in 5 programms , then i count the number of prameters used in call
and the number of parameters used in declaration of procedure imrprime_etiquette
- 09:00 FR: i found a difference of number of prameters between the call and the declaration
- 09:10 FR: i started consulting the log history of svn for the program that cause the problem
- 09:30 FR: i find a commit (merge of other project in the tunk ) it added an in new parameter in the calling
but never changer the declration of imprime_etiquette 
- 10:00 FR: i fixed the problem by adding the new parameter in the declaration procedure 'imprime_etiquette'
- 10:00 FR: i deliver new patch to the prod 
- 12:00 FR: the patch was validated and the impression works correctly 

### Root Cause and Resolution
- we have our own project called RET
- for any new feature we make lots of test before deliver our code to the quality testing
- we merge the code into trunk and create  a new version so we can deliver it
- the  problem there is other team has own project called SEC and it also merge its own code into common trunk 
### Corrective and Preventive Measures
- before any delivery of  new version we must lunch a system called ATS ( testing possibility of regression ) 
to verify the system works as expected ( it is a  suite of automate test cases )
- we also  enhance the communication between teams (RET and SEC) by mail to inform any commit on common trunk  


