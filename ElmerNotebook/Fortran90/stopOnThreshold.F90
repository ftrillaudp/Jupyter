SUBROUTINE getStopOnThreshold(Model, Solver)
  !!! Frederic Trillaud <ftrillaudp@gmail.com> - June, 2021
  !!!celmerf90 -o StopOnThreshold.so StopOnThreshold.F90
  !!! Stop elmer run giving a threshold

  ! Elmer module
  USE DefUtils

  IMPLICIT NONE
  TYPE(Solver_t) :: Solver
  TYPE(Model_t) :: Model
  REAL(KIND=dp), POINTER :: v_component
  TYPE(ValueList_t), POINTER :: params
  TYPE(ValueList_t), POINTER :: time
  REAL(KIND=dp) :: V_th, t_del, t_det
  REAL, ALLOCATABLE, DIMENSION(:) :: timeArray
  LOGICAL :: gotIt, visu

  !!! get parameters from sif file:
  params => GetSolverParams()
  IF (.NOT. ASSOCIATED(params)) THEN
    CALL Fatal('getStopOnThreshold', 'No Parameter found')
  END IF
  V_th = GetConstReal( params, 'Voltage Threshold', gotIt)
  IF (.NOT. gotIt) THEN
    CALL Fatal('getStopOnThreshold', 'Voltage Threshold')
  END IF
  t_del = GetConstReal( params, 'Protection Delay', gotIt)
  IF (.NOT. gotIt) THEN
    CALL Fatal('getStopOnThreshold', 'Protection Delay')
  END IF
  !!! Get the time from computation
  time => gettime()

  IF (v_component >= V_th) THEN
    call AddToDynArray(timeArray, time)
    IF (time >= (timeArray(1) + t_del)) THEN
      CALL ListAddConstReal(Model % Simulation, 'Exit Condition', 1.0_dp)
    END IF
  END IF


CONTAINS
  SUBROUTINE AddToDynArray(array, element)
    IMPLICIT NONE

    integer :: i, isize
    double precision, intent(in) :: element
    double precision, dimension(:), allocatable, intent(inout) :: arrray
    double precision, dimension(:), allocatable :: carray

    if (allocated(array)) then
      isize = size(array)
      allocate(carray(isize+1))
      do i = 1, isize
        carray(i) = array(i)
      end do
      carray(isize+1) = element

      deallocate(array)
      call move_alloc(carray, array)
    else
      allocate(array(1))
      array(1) = element
    end if

  END SUBROUTINE AddToDynArray

END SUBROUTINE getStopOnThreshold
