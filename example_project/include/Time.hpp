#ifndef TIME_HPP
#define TIME_HPP


#include <cstdint>

/**
 * @brief A class handles time
 * @note This class can represents 300 billion years
 *       because 64 bit integer is used for second.
 */
class Time
{
public:

    Time();
    Time(uint64_t sec, uint32_t usec);

    /**
     * @brief Updates time of this instance with now and return this instance.
     */
    Time& now();

    virtual ~Time();

    /**
     * @brief Returns value of this instance in string.
     * @details Format is "[seconds in 12 digits].[microseconds in 6 digits]".
     * @note This operation requires 20 byte buffer.
     *       19 charactors and 1 terminator.
     */
    const char *getStr(char *buffer, size_t size) const;

public:
    bool operator==(const Time &rhs) const;
    bool operator!=(const Time &rhs) const;
    bool operator>(const Time &rhs) const;
    bool operator<(const Time &rhs) const;
    bool operator>=(const Time &rhs) const;
    bool operator<=(const Time &rhs) const;

    Time& operator+=(const Time &rhs);

protected:
    void normalize(void);

private:
    uint32_t usec_; /* Range: 0-999,999 */
    uint64_t sec_;  /* Range: 0- */

};

#endif /* TIME_HPP */
