#include <chrono>
#include <cstring>
#include <cstdio>
#include <cinttypes>

#include <Time.hpp>


#define USEC_MAX (999999)


Time::Time()
:   usec_(0),
    sec_(0)
{
    /* nothing to do */
}

Time::Time(uint64_t sec, uint32_t usec)
:   usec_(usec),
    sec_(sec)
{
    /* nothing to do */
}

Time& Time::now()
{
    std::chrono::time_point<std::chrono::system_clock> now = std::chrono::system_clock::now(); // now in nano seconds
    const uint64_t now_us = now.time_since_epoch().count() / 1000;
    sec_ = now_us / 1000000;
    usec_ = now_us % 1000000;

    return *this;
}


Time::~Time()
{
    /* nothing to do */
}



const char *Time::getStr(char *buffer, size_t size) const
{
    snprintf(buffer, size, "%012" PRIu64 ".%06" PRIu32, this->sec_, this->usec_);
    return buffer;
}

bool Time::operator==(const Time &rhs) const
{
    return this->sec_ == rhs.sec_ && this->usec_ == rhs.usec_;
}

bool Time::operator!=(const Time &rhs) const
{
    return !(*this == rhs);
}

bool Time::operator>(const Time &rhs) const
{
    if ( this->sec_ != rhs.sec_ )
    {
        return this->sec_ > rhs.sec_;
    }
    else
    {
        return this->usec_ > rhs.usec_;
    }
}

bool Time::operator<(const Time &rhs) const
{
    if ( this->sec_ != rhs.sec_ )
    {
        return this->sec_ < rhs.sec_;
    }
    else
    {
        return this->usec_ < rhs.usec_;
    }
}

bool Time::operator>=(const Time &rhs) const
{
    return !(*this < rhs);
}

bool Time::operator<=(const Time &rhs) const
{
    return !(*this > rhs);
}

Time& Time::operator+=(const Time &rhs)
{
    this->sec_ += rhs.sec_;
    this->usec_ += rhs.usec_;
    normalize();
    return *this;
}

void Time::normalize(void)
{
    while ( usec_ > USEC_MAX )
    {
        usec_ -= (USEC_MAX + 1);
        sec_++; // This line cause wrap around
    }
}
