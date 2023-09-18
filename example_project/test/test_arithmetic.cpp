#include <gtest/gtest.h>
#include "arithmetic.hpp"


TEST(TestArithmetic, addOk)
{
    EXPECT_EQ( 0, add(0, 0) );
    EXPECT_EQ( 4, add(1, 3) );
    EXPECT_EQ( -2, add(1, -3) );
    EXPECT_EQ( 2, add(-1, 3) );
    EXPECT_EQ( -4, add(-1, -3) );
}


TEST(TestArithmetic, subOk)
{
    EXPECT_EQ( 0, sub(0, 0) );
    EXPECT_EQ( -2, sub(1, 3) );
    EXPECT_EQ( 4, sub(1, -3) );
    EXPECT_EQ( -4, sub(-1, 3) );
    EXPECT_EQ( 2, sub(-1, -3) );
}
