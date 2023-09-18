#include "AbstractWriter.hpp"


AbstractWriter::AbstractWriter()
{
    /* nothing to do */
}


AbstractWriter::~AbstractWriter()
{
    /* nothing to do */
}


void AbstractWriter::write(const uint8_t *buffer, std::size_t count)
{
    for(int i = 0; i < count; i++)
    {
        writeByte(buffer[i]);
    }
}
