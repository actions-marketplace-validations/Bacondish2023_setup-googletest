#include <cstring>

#include <gtest/gtest.h>
#include <gmock/gmock.h>

#include "AbstractWriter.hpp"


using ::testing::_;


class MockWriter: public AbstractWriter
{
public:
    MOCK_METHOD1(writeByte, void(std::uint8_t data));
};


TEST(TestAbstractWriter, typical)
{
    MockWriter obj;
    const char *message = "Hello, world!!!\r\n";

    EXPECT_CALL(obj, writeByte(_)).Times(17);

    obj.write(reinterpret_cast<const std::uint8_t*>(message), std::strlen(message));
}
