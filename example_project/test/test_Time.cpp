#include <gtest/gtest.h>

#include <Time.hpp>


// -------------------- test fixture --------------------
class TestTimeFixture : public ::testing::Test
{
protected:
    virtual void SetUp()
    {
        time_0_sec_ = Time(0, 0);
        time_1_sec_ = Time(1, 0);
    }

    //virtual void TestDown() {}

    Time time_0_sec_;
    Time time_1_sec_;
};


// -------------------- test case --------------------
TEST_F(TestTimeFixture, typicalWithFixture)
{
    // EXPECT_LE() cause link error in GoogleTest v1.10.0
    EXPECT_FALSE( time_0_sec_ == time_1_sec_ );
    EXPECT_TRUE( time_0_sec_ != time_1_sec_ );
    EXPECT_FALSE( time_0_sec_ > time_1_sec_ );
    EXPECT_TRUE( time_0_sec_ < time_1_sec_ );

    EXPECT_TRUE( time_1_sec_ >  Time(0, 999999) );
    EXPECT_TRUE( time_1_sec_ == Time(1, 00000) );
    EXPECT_TRUE( time_1_sec_ <  Time(1, 000001) );

    EXPECT_TRUE( (time_0_sec_ += Time(1, 0)) == time_1_sec_ );
}

TEST(TestTime, getStr)
{
    const std::size_t size = 32;
    char buffer[size];

    EXPECT_STREQ( "000000000000.999999", Time(0, 999999).getStr(buffer, size) );
    EXPECT_STREQ( "000000000001.000001", Time(1, 000001).getStr(buffer, size) );
}
