function dot(x, y, n) result(d)
    implicit none
    real(kind=8), dimension(n), intent(in) :: x, y
    integer, intent(in) :: n
    real(kind=8) :: d
    integer :: i

    d = 0.0d0
    do i = 1, n
        d = d + x(i) * y(i)
    enddo
end function dot

subroutine matvec(a, x, y, n)
    implicit none
    real(kind=8), dimension(n), intent(in) :: x
    real(kind=8), dimension(n), intent(inout) :: y
    real(kind=8), dimension(n,n), intent(in) :: a
    integer, intent(in) :: n
    integer :: i, j

    y = 0.d0
    do j = 1, n
        do i = 1, n
            y(i) = y(i) + a(i,j) * x(j)
        enddo
    enddo
end subroutine matvec


subroutine pcg(a, b, x, tol, maxit, neq)
    implicit none
    integer, intent(in) :: neq
    !
    real(8), dimension(neq), intent(in) :: b
    real(8), dimension(neq, neq), intent(in) :: a
    real(8), dimension(neq), intent(inout) :: x
    real(8), intent(in) :: tol
    integer, intent(in) :: maxit
    !
    real(8), dimension(:), allocatable :: m, z, r, p
    integer :: i, j
    real(8) :: d, dot, norm_b, conv, alpha, beta, di, xKx, norm_x
    external dot

    !  arranjos auxiliares
    allocate(m(neq), z(neq), r(neq), p(neq))

    ! Precondicionador
    do i=1, neq
        m(i) = 1.d0 / a(i, i)
    enddo

    ! chute inicial
    x = 0.d0

    ! conv = tol * | (M-1) b |m = tol (b, M(-1)b)
    z = m * b
    d = dot(b, z, neq)
    norm_b = dsqrt(dabs(d))
    conv = tol * norm_b

    ! ||b||
    norm_b = dsqrt(dot(b, b, neq))

    call matvec(a, x, z, neq)

    ! r = b - Ax0
    r = b - z

    ! z0 = M(-1)r0
    z = m * r
    p = z
    ! ( r(0),z(0) ) = ( r(0), (M-1)r0 )
    d = dot(r, z, neq)

    do j = 1, maxit

        ! z = Ap(j)
        call matvec(a, p, z, neq)

        ! alpha =( r(j),z(j) ) / ( Ap(j), p(j) ))
        alpha = d / dot(p, z, neq)

        do i=1, neq
            ! x(j+1) = x(j) + alpha*p
            x(i) = x(i) + alpha * p(i)
            ! r(j+1) = r(j) - alpha*Ap*/
            r(i) = r(i) - alpha * z(i)
        enddo

        ! z  = (M-1)r0
        z = m * r

        ! (r(j + 1), (M - 1)r(j + 1)) = (r(j + 1), z)
        di = dot(r, z, neq)
        ! beta = ( r(j+1),(M-1)r(j+1) ) / ( r(j),r(j) )
        beta = di / d

        ! p(j+1) = (M-1)r(j+1) + beta*p(j) = z + beta*p(j)
        do i=1, neq
            p(i) = z(i) + beta * p(i)
        enddo

        d = di;
        if (dsqrt(dabs(d)) < conv) exit;

    enddo

    ! Energy norm:  x*Kx
    call matvec(a, x, z, neq);
    ! norma de energia = xTAx
    xKx = dot( x, z, nEq);

    ! norm = || x ||
    norm_x = sqrt(dot(x, x, neq));

    print *,j, xKx, norm_x, x, tol, neq

    ! free
    deallocate(m, z, r, p)

end subroutine pcg
