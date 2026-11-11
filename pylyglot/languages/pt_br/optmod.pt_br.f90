! pylyglot: pt_br # version: 1.1.1 #
!* Implementation of optimization methods and main procedures.\

módulo optmod
!* Module implementing the optimization methods and main procedures for\
! reading the "main.txt" file, launching the optimization, and reporting\
! results.\
!\
! When adding more optimization methods, variables ``nb_methods`` and\
! ``method_names`` must updated.\
!\
! When adding more report parameters, variables ``nb_rprt_params`` and\
! ``rport_params``) must be updated.\
usar funcmod
implícito nenhum

! Related to the methods themselves:\
inteiro, parâmetro :: nb_methods = 2
!! Number of methods implemented\
caracter*20, dimension(nb_methods), parâmetro :: method_names =     (/ "GD     ",         "NR     "/)
!! The names of the methods themselves\

! Related to report parameters:\
inteiro, parâmetro :: nb_rprt_params = 3
!! Number of report parameters.\
caracter*256, dimension(nb_rprt_params), parâmetro :: rprt_params =     (/ "freq  ",         "format",         "print " /)
! The number of times a method should be run\
! Formatting string\
! Whether or not to print results in command line\
! This still has to\
! be implemented, but\
! should maybe\
! integrate a few\
! printing options\
!! Names of the report parameters.\
\
contém
! OPTIMIZATION METHODS: =======================================================================================\
subrotina GD(format_str, output_str)
!* GRADIENT DESCENT\
!\
! Gradient Descent method.\
! This optimization method is based in the fact that the\
! gradient of a function points in its maximum growth\
! direction. In order to minimize it, we'll go in the\
! opposite direction (\(-\nabla f\)). Of course, this is done\
! by updating x (and \(\nabla f\)) iteratively.\
!\
! \(x = x - LR * \nabla f(x)\)\
!\
! HYPER PARAMETERS\
! ----------------\
! > ``x : real*8, dimension(dimx)``\
!       Initial guess. Must have as many dimensions as\
!       the input variable has (obviously).\
!\
! > ``LR : real*8``\
!       Learning Rate. Related to the iteration step.\
!\
! > ``eps : real*8``\
!       Minimum relative error for stopping. If a\
!       relative step (step divided by the current x) is\
!       smaller than eps, then the process stops and we\
!       consider the optimization as done.\
!\
! > ``Nmax : integer, optional. Default = 1,000,000``\
!       Maximum number of iterations.\
!\
\
implícito nenhum
! Hyper parameter subroutine:\
inteiro :: nb_hprparams = 4
!! Number of hyperparameters\
inteiro :: size_hprdata
!! Size of hprdata's second dimension\
caracter*256, dimension(:), alocável :: hprnames
!! Hyperparameter names.\
real*8, dimension(:, :), alocável :: hprdata
!! Where data will be saved\
inteiro, dimension(:), alocável :: hprdim
!! Dimension of each hprparam.\
lógico, dimension(:), alocável :: hprbool, requiredbool
!! Bool array: hprparam present or not\
\
! Actual hyper parameters:\
real*8 :: LR
!! Learning Rate\
real*8 :: eps
!! Minimum relative error for stopping\
inteiro :: Nmax
!! Max. number of iterations\
\
! Actual method:\
inteiro :: it1, it2
real*8, dimension(dimx) :: x
!! Input variable\
real*8, dimension(dimx) :: dy_dx
!! Gradient value at x\
real*8 :: y
!! Function value at x\
real*8, dimension(dimx) :: re
!! Relative error\
lógico :: stopbool
\
! Report variables:\
caracter*1000 :: value_str
!! Actual x and y values for reportting.\
caracter*1000 :: output_str
!! Actual x and y values for reportting.\
caracter*1000 :: halting_str
!! Halting reason\
caracter*3 :: dimx_str
!! dimx as a string\
caracter*20 :: format_str
!! formatting string\
!--------------------------------------------------------------------------------------------------------------\
\
\
size_hprdata = dimx
alocar(hprnames(nb_hprparams))
alocar(hprdata(nb_hprparams, size_hprdata))
alocar(hprdim(nb_hprparams))
alocar(hprbool(nb_hprparams))
alocar(requiredbool(nb_hprparams))
\
hprnames = (/ "x          ",  "LR         ",  "eps        ",  "Nmax       "/)
! Hpr param names\
hprdata = 0
! (not really necessary)\
hprdim = (/dimx, 1, 1, 1/)
! Dimension of each of the hprparams\
hprbool = .false.
! Initializing hprbool array as .false.\
requiredbool = (/.true., .true., .true., .false./)
! specifying which hprparams are optional\
\
! DEFAULT VALUES FOR OPTIONAL HYPERPARAMETERS:\
hprdata(4, 1) = 1000000
! Nmax\
\
chamar handle_hyp_file(nb_hprparams, size_hprdata, hprnames, hprdata, hprdim, hprbool, requiredbool)
\
x = hprdata(1, :hprdim(1))
LR = hprdata(2, 1)
eps = hprdata(3, 1)
Nmax = int(hprdata(4, 1))
\
y = fn(x)
\
chamar format_data(x, y, format_str, value_str)
output_str = aparar(value_str)
halting_str=""
fazer it1 = 1, Nmax
dy_dx = dfn_dx(x)
x = x - LR*dy_dx
re = abs(LR*dy_dx/x)
\
fazer it2 = 1, dimx
stopbool = .true.
se (re(it2) .ge. eps) então
stopbool = .false.
exit
fim se
fim fazer
\
se (stopbool) então
imprimir *, "Stopping iteration: ", it1
halting_str = "Precision condition reached;"
exit
fim se
\
fim fazer
se (halting_str == "") então
halting_str = "Max. number of iterations reached;"
fimse
y = fn(x)
chamar format_data(x, y, format_str, value_str)
output_str = aparar(output_str)//"    "//aparar(value_str)//  "    "//aparar(halting_str)
\
fim subrotina GD
! HANDLING FUNCTIONS ==========================================================================================\
subrotina handle_main_file(nb_methods, nb_rprt_params, method_names, rprt_params)
!* Subroutine for handling the optimization runs.\
!\
! This subroutine reads the ``main.txt`` file and\
! interpets its contents.\
!\
! - This means reading the optimization methods, the\
!   report parameters (types of output, number of\
!   times a certain optimization should be run, etc.) and\
!   calling the corresponding optimization subroutine and\
!   passing it the important hyperparameter information.\
!\
! - As of know, in order to maintain the current\
!   implementation, the method's hyperparameters are\
!   written to the ``output/hyperparams.txt`` file (deleted\
!   at the end of execution). This is\
!   surely not the best way to do this (passing the\
!   ``character`` variable directly to the method ought\
!   to be more efficient). This is an improvement that\
!   can be done in the future (changing the\
!   ``handle_hyp_file`` subroutine) and how its called in\
!   the optimization methods.\
\
! This subroutine's arguments:\
inteiro :: nb_methods
!! The total number of optimization methods currently implemented\
inteiro :: nb_rprt_params
!! Number of report parameters currently implemented.\
caracter*20, dimension(nb_methods) :: method_names
!! Array of optimization methods' names/labels.\
caracter*256, dimension(nb_rprt_params) :: rprt_params
!! Array of report parameters' names/labels.\
\
! Variables related to this subroutines\
inteiro, dimension(1000) :: line_counter=0
!! "Saves" line numbers\
inteiro :: line_number=0, line_idx=0, nb_lines, nb_runs
caracter*1000 :: hprparam_str
!! Values for the optim. methods' hpr params\
caracter*20 :: optim_method
!! Name of the optimization method for a run\
! Report parameter related\
caracter*256, dimension(nb_rprt_params) :: rprt_data
!! Values of the rprt params\
inteiro :: repetitions, rep_iteration
!! ``freq`` param.\
caracter*20 :: format_str
!! ``format`` param\
! Report related:\
caracter*1000 :: hprparam_str2
!! Hyperparameter string\
caracter*100000 :: rprt_str
!! The report string\
caracter*1000 :: output_str
!! Opt. method output string\
caracter*1000 :: hdr_str, hdr_str2
!! Strings for the header\
caracter*5 :: repetition_str
inteiro :: iter_dimx
!! iterate in dimx\
caracter*3 :: dim_str
!! dimension string\
\
! File reading related:\
inteiro :: filestatus
!! File reading status (indicates errors)\
caracter*256 :: errormsg, read_line
!! Error message and read line\
caracter*256 :: key_word
!! Line keyword (hyperparam. name)\
inteiro, dimension(1) :: result1
!! Indexes corresponding to optim. methods\
inteiro, dimension(1) :: result2
!! Indexes corresponding to report params\
inteiro :: idx1, idx2
!! The actual indexes\
inteiro :: main_file, hpr_file, rprt_file
!! For generality, may be useful in the future.\
!--------------------------------------------------------------------------------------------------------------\
\
! Opening the file\
main_file = 00000
open(main_file, file="main.txt", status="old",  iostat = filestatus, iomsg = errormsg)
! Opening the file\
chamar check_status(filestatus, errormsg)
! Handling errors\
\
! Finding where the optim. methods are defined.\
! The next bit has been adapted from: the following StackOverflow response:\
! https://stackoverflow.com/questions/29125581/fortran-find-string-in-txt-file\
fazer
read(main_file, "(a)", iostat=filestatus) read_line
! Read line\
se (filestatus /= 0) então
! When we've reached the end of the file\
exit
fim se
line_number = line_number + 1
! Increase line number (1st line is line 1).\
\
read(read_line, *) key_word
! Getting keyword (optim. method/param.)\
\
result1 = findloc(method_names, key_word)
! Getting its index in the optimization method list\
idx1 = result1(1)
! just for clarity\
\
se (idx1 == 0) então
! If it isn't an optim. method label, then skip line\
cycle
fim se
\
! ELSE: Optimization method name found:\
line_idx = line_idx + 1
! Update index (starts at 1)\
line_counter(line_idx) = line_number
! Save the line number which contains the opt. label\
fim fazer
nb_runs = line_idx
nb_lines = line_number
\
! We add the end of the file to the list, will be useful\
! later for halting the code:\
line_counter(nb_runs+1) = nb_lines+1
\
! Closing file (only to be reopened again at its beginning)\
close(main_file)
! Closing file\
open(main_file, file="main.txt", status="old",  iostat = filestatus, iomsg = errormsg)
! Opening the file\
chamar check_status(filestatus, errormsg)
\
! Resetting line idx and number:\
line_idx = 1; line_number = 0;
\
! Writting the header for the report:\
rprt_str = "OPT. METHOD;    HYPER PARAMETERS;    SUB-RUN;"
hdr_str = ""
hdr_str2 = ""
fazer iter_dimx = 1, dimx
escrever(dim_str, "(I3)") iter_dimx
hdr_str = aparar(hdr_str)//"    X0("//aparar(adjustl(dim_str))//");"
hdr_str2 = aparar(hdr_str2)//"    XF("//aparar(adjustl(dim_str))//");"
fim fazer
rprt_str = aparar(rprt_str)//aparar(hdr_str)//"    Y0;"//  aparar(hdr_str2)//"    YF;    Stopping reason;"
\
rprt_file = 10000
open(rprt_file, file="output/report.txt",  iostat = filestatus, iomsg = errormsg)
! Opening the file\
chamar check_status(filestatus, errormsg)
! Handling errors\
escrever(rprt_file, '(a)') aparar(rprt_str)
close(rprt_file)
\
! Now actually calling the optimization procedures:\
fazer
\
! Reading current line\
read(main_file, "(a)", iostat=filestatus) read_line
! Read line\
se (filestatus /= 0) então
! End if end of file\
exit
fim se
line_number = line_number + 1
! Updating line nb.\
\
! Tried using the "select case" statement for this,\
! but apparently cases cannot be written in function\
! of variales, so...\
se (line_number == line_counter(line_idx)) então
! If it's the line of an optimization label:\
read(read_line, *) optim_method
! Save it as ``optim_method``\
hprparam_str=""
! Reset method's hyperparameters\
hprparam_str2=""
! Reset method's hyperparameters\
rprt_data = (/"1      ",  "(f11.4)",  ".false."/)
! Reset report parameters\
\
senão se (line_number == (line_counter(line_idx + 1) - 1)) então
! If its the last line of a method:\
line_idx = line_idx + 1
! Update line_idx\
\
! Check for report hprparams and adding them to\
! the hprparam_str\
read(read_line, *) key_word
! This part is the same code as the last (else) condition\
result2 = findloc(rprt_params, key_word)
! Searching for report parameters\
idx2 = result2(1)
\
se (idx2 /= 0) então
! If they're present, save.\
read(read_line, *) key_word, rprt_data(idx2)
senão
! If it's something else, they're optim. hpr params\
hprparam_str = aparar(hprparam_str)//NEW_LINE('A')//read_line
hprparam_str2 = aparar(hprparam_str2)//", "//read_line
fim se
\
! Since this is this run's last line, then we can\
! save the hyperparameters in a file.\
hpr_file = 00001
open(hpr_file, file="output/hyperparams.txt",  iostat = filestatus, iomsg = errormsg)
! Opening the file\
chamar check_status(filestatus, errormsg)
! Just in case\
escrever(hpr_file, '(a)') aparar(hprparam_str(2:))
close(hpr_file)
\
! Reading report parameters:\
read(rprt_data(1), *) repetitions
read(rprt_data(2), "(a)") format_str
\
fazer rep_iteration = 1, repetitions
select case(optim_method)
case("GD")
chamar GD(format_str, output_str)
fim select
\
escrever(repetition_str, '(I5)') rep_iteration
rprt_str = aparar(optim_method)//";    "//aparar(hprparam_str2(3:))  //";    "//aparar(adjustl(repetition_str))//";    "//aparar(output_str)
\
! Adding results to the report:\
open(rprt_file, file="output/report.txt", position="append",  iostat = filestatus, iomsg = errormsg)
chamar check_status(filestatus, errormsg)
escrever(rprt_file, '(a)') aparar(rprt_str)
close(rprt_file)
fimfazer
senão
! Check for report hprparams and adding them to\
! the hprparam_str\
read(read_line, *) key_word
! This part is the same code as the last (else) condition\
result2 = findloc(rprt_params, key_word)
! Searching for report parameters\
idx2 = result2(1)
se (idx2 /= 0) então
! If they're present, save.\
read(read_line, *) key_word, rprt_data(idx2)
senão
! If it's something else, they're optim. hpr params\
hprparam_str = aparar(hprparam_str)//NEW_LINE('A')//read_line
hprparam_str2 = aparar(hprparam_str2)//", "//read_line
fim se
fim se
fim fazer
\
close(main_file)
! Closing file\
! Deleting hyperparams file since it is no longer needed:\
open(hpr_file, file="output/hyperparams.txt",  iostat = filestatus, iomsg = errormsg)
! Opening the file\
se (filestatus == 0) então
close(hpr_file, status="delete")
! Delete file\
senão
chamar check_status(filestatus, errormsg)
! Just in case\
fim se
\
fim subrotina handle_main_file
\
subrotina handle_hyp_file(nb_hprparams, size_hprdata, hprnames, hprdata, hprdim, hprbool, requiredbool)
!* Subroutine for handling the method's hyper parameters.\
!\
! This subroutine reads the ``hyperparams.txt`` and\
! stores the values informed by the user.\
! - It reads the file line by line. When the first word\
!   in a line matches with one of the hyper parameter's\
!   name (contained in ``hprnames``, defined in the\
!   method of choice), it saves its value in the\
!   ``hprdata`` array.\
!\
! ARGUMENTS\
! ---------\
! > ``np_hprparams : integer``\
!       The total number of hyper parameters possible for the\
!       optimization method.\
!\
! > ``size_hprdata : integer``\
!       Size of hprdata second dimension (usually dimx,\
!       extended for generality).\
!\
! > ``hprnames : character*256, dim(nb_hprparams)``\
!       Array of hyper parameter names/labels.\
!\
! > ``hprdata : real*8, dim(nb_hprparams, size_hprdata)``\
!       Array of data (each hyperparameter value). Will\
!       have a lot of unused elements, since not all\
!       hyper parameters will have the same dimension.\
!       Each line is a different hyper parameter, in the\
!       same order as in hprnames.\
!\
! > ``hprdim : integer, dim(nb_hprparams)``\
!       Dimension of each hyper parameter, again in order.\
!\
! > ``hprbool : logical, dim(nb_hprparams)``\
!       Boolean array indicating which hyper parameters\
!       have been informed by the user (.true.) and which\
!       weren't (.false.).\
!\
! > ``requiredbool : logical, dim(nb_hprparams)``\
!       Which hyper parameters are required (.true.) and\
!       which are optional (.false.). This argument is\
!       not used in this subroutine, but directly in\
!       ``check_hprparams``, which is called directly at\
!       the end of this subroutine, but was separated\
!       solely for clarity.\
\
! This subroutine:\
inteiro :: nb_hprparams
!! The total number of hyper parameters possible for the\
!! optimization method.\
inteiro :: size_hprdata
!! Size of hprdata second dimension (usually dimx,\
!! extended for generality).\
caracter*256, dimension(nb_hprparams) :: hprnames
!! Array of hyper parameter names/labels.\
real*8, dimension(nb_hprparams, size_hprdata) :: hprdata
!! Array of data (each hyperparameter value). Will\
!! have a lot of unused elements, since not all\
!! hyper parameters will have the same dimension.\
!! Each line is a different hyper parameter, in the\
!! same order as in hprnames.\
inteiro, dimension(nb_hprparams) :: hprdim
!! Dimension of each hyper parameter, again in order.\
lógico, dimension(nb_hprparams) :: hprbool
!! Boolean array indicating which hyper parameters\
!! have been informed by the user (.true.) and which\
!! weren't (.false.).\
! Hyper parameter check subroutine:\
lógico, dimension(nb_hprparams) :: requiredbool
! Bool array: hprparam optional or not\
!! Which hyper parameters are required (.true.) and\
!! which are optional (.false.). This argument is\
!! not used in this subroutine, but directly in\
!! ``check_hprparams``, which is called directly at\
!! the end of this subroutine, but was separated\
!! solely for clarity.\
\
! File reading related:\
inteiro :: filestatus
!! File reading status (indicates errors)\
caracter*256 :: errormsg, read_line
!! Error message and read line\
caracter*5 :: key_word
!! Line keyword (hyperparam. name)\
inteiro, dimension(1) :: result
!! Indexes corresponding to the hyperparam. array\
inteiro :: idx
!! The actual index\
inteiro :: file_number
!! For generality, may be useful in the future.\
\
\
! Opening the file\
file_number = 00001
open(file_number, file="output/hyperparams.txt", status="old",  iostat = filestatus, iomsg = errormsg)
! Opening the file\
\
chamar check_status(filestatus, errormsg)
! When we've reached the end of the file\
\
! Reading the hyperparameters:\
! The next bit has been adapted from: the following StackOverflow response:\
! https://stackoverflow.com/questions/29125581/fortran-find-string-in-txt-file\
fazer
read(file_number, "(a)", iostat=filestatus) read_line
! Read line\
se (filestatus /= 0) então
! Error handling\
exit
fim se
read(read_line, *) key_word
! Getting keyword (hyperparam.)\
result = findloc(hprnames, key_word)
! Getting its index\
idx = result(1)
! just for clarity\
\
! NOTE: Fortran runtime error: End of file will ensue\
! if the hyperparameter informed has less dimensions\
! than necessary.\
read (read_line, *) key_word, hprdata(idx, :hprdim(idx))
hprbool(idx) = .true.
fim fazer
\
! Closing file\
close(file_number)
! Closing file\
\
! Checking required and optional hyperparameters:\
chamar check_hprparams(nb_hprparams, hprnames, hprdata, hprdim, hprbool, requiredbool)
fim subrotina handle_hyp_file
\
subrotina check_status(filestatus, errormsg)
!* Subroutine for handling file reading errors.\
!\
! This subroutine takes directly the ``iostat`` and\
! ``iomsg`` values from the file opening procedure.\
!\
! ARGUMENTS\
! ---------\
! > ``filestatus : integer``\
!       The ``iostat`` value.\
!\
! > ``errormsg : character*256``\
!       The associated error message.\
!\
\
inteiro :: filestatus
!! File reading status (indicates errors)\
caracter*256 :: errormsg
!! Error message and read line\
\
se (filestatus /= 0) então
! Handling error\
imprimir *, "Error when reading the hyperparameter file:",  NEW_LINE('A')//" -> ", errormsg
stop
fimse
fim subrotina check_status
\
subrotina check_hprparams(nb_hprparams, hprnames, hprdata, hprdim, hprbool, requiredbool)
!* Subroutine for checking which hyper parameters were informed by the user.\
!\
! This subroutine starts where the ``handle_hyp_file(...)``\
! subroutine stops, and is written separately only for\
! clarity. It checks if all required hyper parameters\
! have been defined (and will halt execution if not). If\
! optional hyper parameters haven't been specified, then\
! it warns the user and shows them the default values\
! used.\
!\
! @note\
! Default values for optional hyper parameters must be\
! defined in the optimization procedure before calling the\
! ``handle_hyp_file(...)`` subroutine, by initializing the\
! associated elements of the hprdata array.\
! @endnote\
!\
! - ARGUMENTS are explained in the ``handle_hyp_file(...)``\
!   subroutine's documentation\
\
\
inteiro :: nb_hprparams, idx
! Hyperparameter arrays\
caracter*256, dimension(nb_hprparams) :: hprnames
!! Hyperparameter names.\
real*8, dimension(nb_hprparams, dimx) :: hprdata
!! Where data will be saved\
inteiro, dimension(nb_hprparams) :: hprdim
!! Dimension of each hprparam.\
lógico, dimension(nb_hprparams) :: hprbool
!! Bool array: hprparam present or not\
lógico, dimension(nb_hprparams) :: requiredbool
!! Bool array: hprparam optional or not\
! For checking the hyperparams:\
caracter*256 :: uninformed_required, uninformed_optional
!! Hyperparameters nor informed by the user\
caracter*256 :: default_value
!! Default values of optional hprparams\
lógico :: haltbool = .false.
!! Whether the program should be halted or not\
\
!! Checking if all hyperparameters were informed:\
uninformed_required = ""
uninformed_optional = ""
fazer idx = 1, nb_hprparams
se (.not. hprbool(idx)) então
! If it wasn't informed\
se (requiredbool(idx)) então
! And it was required\
haltbool = .true.
! Program will be halted\
uninformed_required = aparar(uninformed_required)//", "//aparar(hprnames(idx))
! Adding to the list of missing parameters\
\
senão
! If it was optional, then we'll warn the user\
escrever(default_value, *) hprdata(idx, :hprdim(idx))
uninformed_optional = aparar(uninformed_optional)//" -> "//  aparar(hprnames(idx))//  " = "//aparar(default_value)//  NEW_LINE('A')
! Name of the optional hprparam\
! Default value of the optional hprparam\
fim se
fim se
fim fazer
se (haltbool) então
! If a required hyperparam was missing: Halt code\
uninformed_required = uninformed_required
imprimir *, "The following REQUIRED hyperparameters were not informed by the user:"
imprimir *, " -> "//uninformed_required(3:)
! 3: to take out the ", "\
stop
fim se
se (uninformed_optional /= "") então
! If an optional parameter was missing: Warn user\
imprimir *, "The following OPTIONAL hyperparameters were not informed by the user and their default values will be used."
imprimir *, " "//aparar(uninformed_optional)
fim se
fim subrotina check_hprparams
\
subrotina format_data(x, y, format_str, value_str)
!* Small function for formatting data according to a format string.\
! Argument ``value_str`` is the output string containing the\
! ``x`` and ``y`` values.\
\
real*8, dimension(dimx), intent(in) :: x
!! Input variable\
real*8, intent(in) :: y
!! Function value at x\
\
inteiro :: iter_dim
!! Iterator on x dimension\
caracter*100 :: var_str
!! Variable string\
caracter*20 :: format_str
!! Formatting string\
caracter*1000 :: value_str
!! Output string\
\
value_str = ""
fazer iter_dim = 1, dimx
escrever(var_str, format_str) x(iter_dim)
value_str = aparar(value_str)//"    "//aparar(adjustl(var_str))//";"
fim fazer
escrever(var_str, format_str) y
value_str = aparar(adjustl(value_str))//"    "//aparar(adjustl(var_str))//";"
\
fim subrotina format_data
fim módulo optmod